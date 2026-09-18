"""Stage 4 - grounding (free), enrichment (paid), rendering, routing index.

The split between what a script does and what a model does is the design.
Retrieving a quotation and locating its page are string operations: a script does
them exactly, for free, every time.  Summarising a regulatory theme is synthesis,
and that is what the model is for.

  ground()  - deterministic.  Excerpts are *sliced out of* the source, so they
              are verbatim by construction and their page number is known from
              the byte offset.  Caveats are computed from graph metadata and
              corpus quality.  No tokens.
  enrich()  - the model does only what nothing else can: per-node summaries,
              community themes, and narratives for edges that earn one.
  render()  - writes the vault notes.
  routing_index() - writes the vault's own entry point, _INDEX_Routing.md.
"""

from __future__ import annotations

import json
import os
import random
import re
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from . import config
from .common import (
    keywords, md_table, page_for_offset, parse_md_pages, pf_share, read_json,
    resolve_source, sentences, stem_of_source, strip_presentation_forms,
    utf8_console, wikilink, write_json,
)

# --------------------------------------------------------------------------- #
# Graph access
# --------------------------------------------------------------------------- #

def load_graph() -> Tuple[Dict[str, dict], List[dict]]:
    raw = read_json(config.GRAPH_JSON)
    if not raw:
        raise SystemExit(f"Missing {config.GRAPH_JSON} — run the build stage first.")
    nodes = {n["id"]: n for n in raw["nodes"]}
    links = raw.get("links") or raw.get("edges") or []
    return nodes, links


def edge_key(e: dict) -> str:
    a, b = sorted([e["source"], e["target"]])
    return f"{a}||{b}||{e.get('relation', '')}"


def node_sources(node: dict) -> List[str]:
    """Every source document backing a node (dedup may have merged several)."""
    out = list(node.get("source_files") or [])
    if node.get("source_file") and node["source_file"] not in out:
        out.insert(0, node["source_file"])
    return out


def degrees(links: Sequence[dict]) -> Dict[str, int]:
    d: Dict[str, int] = defaultdict(int)
    for l in links:
        d[l["source"]] += 1
        d[l["target"]] += 1
    return d


# --------------------------------------------------------------------------- #
# Deterministic grounding
# --------------------------------------------------------------------------- #

_source_cache: Dict[str, Optional[dict]] = {}


def _load_source(source_file: str) -> Optional[dict]:
    """Parse a corpus file once and keep its sentence index.

    Grounding touches the same handful of documents thousands of times (once per
    incident edge), so splitting sentences per call is the difference between a
    four-minute stage and a few seconds.  Sentences are pre-lowercased for
    scoring and pre-tagged with their page number.
    """
    if source_file in _source_cache:
        return _source_cache[source_file]
    path = resolve_source(source_file)
    if not path:
        _source_cache[source_file] = None
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    pages = parse_md_pages(text)
    index = []
    for page in pages:
        for sent, off in sentences(page.body, page.start):
            if 40 <= len(sent) <= 400:
                clean = re.sub(r"\s+", " ", sent).strip()
                index.append((clean, clean.lower(), page.number, off))
    _source_cache[source_file] = {"text": text, "pages": pages, "sentences": index,
                                  "pf_share": pf_share(text)}
    return _source_cache[source_file]


def best_excerpt(node: dict, other_label: str) -> Optional[dict]:
    """Pick the sentence in a node's source that best supports this link.

    Scored on the node's own label terms (weighted) plus the neighbour's, with a
    mild preference for sentences of quotable length.  Whatever comes back is a
    literal slice of the file, so it can never fail a verbatim check.
    """
    own = keywords(node.get("label", ""))
    other = keywords(other_label)
    if not own and not other:
        return None

    best = None
    for source_file in node_sources(node):
        src = _load_source(source_file)
        if not src:
            continue
        for clean, low, page_no, off in src["sentences"]:
            score = 2 * sum(low.count(k) for k in own) + sum(low.count(k) for k in other)
            if not score:
                continue
            if 80 <= len(clean) <= 260:
                score += 0.5
            if best is None or score > best["score"]:
                best = {"score": score, "excerpt": clean[:config.MAX_EXCERPT_CHARS],
                        "page": page_no, "source_file": source_file, "offset": off}
    if best:
        best.pop("score", None)
    return best


def _caveats(edge: dict, na: dict, nb: dict, ex_a, ex_b) -> Optional[str]:
    """Caveats derived from data already held, rather than asked of the model."""
    notes = []
    conf = (edge.get("confidence") or "").upper()
    if conf in ("INFERRED", "AMBIGUOUS"):
        notes.append(f"Link is {conf.lower()}, not stated in the text — verify the primary "
                     "instrument before relying on it.")
    if (edge.get("relation") or "") in config.WEAK_RELATIONS:
        notes.append("Relation is a similarity heuristic, not a cross-reference.")
    for node, ex, side in ((na, ex_a, "A"), (nb, ex_b, "B")):
        for sf in node_sources(node):
            src = _load_source(sf)
            if src and src["pf_share"] >= config.PF_SHARE_OCR:
                notes.append(f"Source {stem_of_source(sf)} still contains broken Arabic — "
                             "treat quotes from it as indicative only.")
                break
    if ex_a is None or ex_b is None:
        notes.append("No supporting sentence found on at least one side.")
    return " ".join(dict.fromkeys(notes)) or None


def ground(nodes: Dict[str, dict], links: List[dict]) -> dict:
    out: Dict[str, dict] = {}
    total = len(links)
    for i, e in enumerate(links, 1):
        if i % 250 == 0:
            print(f"  grounded {i}/{total}", flush=True)
        ia, ib = sorted([e["source"], e["target"]])
        na, nb = nodes.get(ia), nodes.get(ib)
        if not na or not nb:
            continue
        ex_a = best_excerpt(na, nb.get("label", ""))
        ex_b = best_excerpt(nb, na.get("label", ""))
        out[edge_key(e)] = {
            "clause_a": ex_a, "clause_b": ex_b,
            "caveat": _caveats(e, na, nb, ex_a, ex_b),
            "relation": e.get("relation"), "confidence": e.get("confidence"),
        }
    grounded = sum(1 for v in out.values() if v["clause_a"] and v["clause_b"])
    write_json(config.GROUNDING_JSON, {
        "generated": datetime.now(timezone.utc).isoformat(),
        "edges": len(out), "both_sides_grounded": grounded, "grounding": out,
    })
    print(f"Grounding: {grounded}/{len(out)} edges have a verbatim excerpt on both sides "
          f"(excerpts are sliced from source, so verbatim by construction)")
    return out


# --------------------------------------------------------------------------- #
# Model layer
# --------------------------------------------------------------------------- #

PERSONA = """\
You are a SAMA regulatory compliance/legal analyst working on a Saudi Central Bank
(SAMA) knowledge base used by compliance and legal teams to answer questions about
KSA financial-sector rules.

Domain stance:
- Read obligations as enforceable requirements (who must do what, when, to whom).
- Distinguish regimes: AML/CTF, payments/PSP, BNPL/finance companies, consumer
  protection, data/credit information, sanctions/TFS, governance/risk. Flag
  cross-regime interactions (e.g. BNPL "Consumer" vs AML "Customer";
  merchant-as-customer / KYB; third-party CDD reliance).
- Preserve defined terms; note scope limits; never invent article numbers or text
  that is not in the provided context.

Do NOT give RegTech, system-design, tooling or implementation advice. Stay at the
level of legal/regulatory meaning and its consequence for a decision.

Never quote source text in your output. Verbatim excerpts are supplied separately
by a deterministic extractor; your job is meaning, not quotation.

Tone: precise, neutral, practical, brief. Return ONLY valid JSON, no markdown fences.
"""

SYS_NODES = PERSONA + """
Task: for each instrument/concept node, write a compact orientation entry that helps
a researcher decide whether to open the underlying document.

{
  "id": "<same as input>",
  "summary": "2-3 sentences: what this node is, what it governs or defines, and who it binds.",
  "regimes": ["AML/CTF" | "payments" | "BNPL/finance" | "consumer protection" | "data/credit info" | "sanctions/TFS" | "governance/risk" | "banking prudential" | "other"],
  "lookup_terms": ["3-8 terms a colleague would search for to land on this node, including defined terms and common synonyms"]
}
Output {"nodes":[...]} covering every input id exactly once.
"""

SYS_COMMUNITIES = PERSONA + """
Task: write a short blurb for each community (cluster) of the graph.

{
  "community_id": <int>,
  "theme": "1-2 sentences: the regulatory problem-space this cluster covers",
  "how_members_connect": ["2-4 bullets on the legal linkage - shared definitions, obligation chains, cross-references, or hierarchy (law -> regulation -> circular -> guide)"],
  "start_here": ["1-3 member labels a researcher should read first"]
}
Output {"communities":[...]} covering every input community_id exactly once.
"""

SYS_EDGES = PERSONA + """
Task: explain what a link between two instruments means for a compliance decision.

{
  "edge_key": "<same as input>",
  "why": "2-4 sentences. LEAD with the practical decision framing. FOLD IN the regulatory basis (shared parent law, defined term, cross-reference, obligation chain, hierarchy). END with the consequence for the reader. If confidence is INFERRED or AMBIGUOUS, write tentatively and say the reader should verify the primary text."
}
Output {"edges":[...]} covering every input edge_key exactly once.
"""

_usage_lock = threading.Lock()
_log_lock = threading.Lock()


def _append_jsonl(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with _log_lock:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def _record_usage(payload: dict) -> None:
    u = payload.get("usage") or {}
    inp = u.get("input_tokens", 0)
    cached = u.get("cache_read_input_tokens", 0)
    out = u.get("output_tokens", 0)
    p_in, p_out = config.PRICES.get(config.ENRICH_MODEL, (0.0, 0.0))
    cost = (inp * p_in + cached * p_in * 0.1 + out * p_out) / 1_000_000
    with _usage_lock:
        _append_jsonl(config.USAGE_LOG, {
            "ts": datetime.now(timezone.utc).isoformat(), "model": config.ENRICH_MODEL,
            "input_tokens": inp, "cache_read_input_tokens": cached,
            "output_tokens": out, "est_cost_usd": round(cost, 6),
        })


def claude_json(system: str, user: str, api_key: str, max_tokens: int = 8192) -> dict:
    """One API call, with backoff so a rate limit becomes a delay, not a gap.

    The system prompt is marked cacheable: it is identical across every call in a
    stage, so there is no reason to pay for it more than once.
    """
    body = {
        "model": config.ENRICH_MODEL,
        "max_tokens": max_tokens,
        "system": [{"type": "text", "text": system,
                    "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": user}],
    }
    data = json.dumps(body).encode("utf-8")
    headers = {
        "content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": config.ANTHROPIC_VERSION,
    }
    if config.ENRICH_WORKSPACE_ID:
        headers["anthropic-workspace-id"] = config.ENRICH_WORKSPACE_ID

    last = None
    for attempt in range(config.ENRICH_MAX_RETRIES):
        req = urllib.request.Request(config.API_URL, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:400]
            if "anthropic-workspace-id" in detail and not config.ENRICH_WORKSPACE_ID:
                raise SystemExit(
                    "This API key is identity-linked and must name a workspace.\n"
                    "  Find the id in the Anthropic Console (Settings -> Workspaces);\n"
                    "  it looks like 'wrkspc_...'. Then set it:\n"
                    '    SAMA_ENRICH_WORKSPACE_ID="wrkspc_..."   (add to .env)'
                ) from e
            last = RuntimeError(f"HTTP {e.code}: {detail}")
            # 429 / 5xx are transient; anything else is a real error.
            if e.code not in (408, 409, 429, 500, 502, 503, 504, 529):
                raise last from e
        except Exception as e:  # network hiccup
            last = e
        sleep = config.ENRICH_BACKOFF_BASE ** attempt + random.uniform(0, 1)
        print(f"    retry {attempt + 1}/{config.ENRICH_MAX_RETRIES} in {sleep:.1f}s ({last})",
              flush=True)
        time.sleep(sleep)
    else:
        raise RuntimeError(f"exhausted retries: {last}")

    _record_usage(payload)
    text = "\n".join(b.get("text", "") for b in payload.get("content", [])
                     if b.get("type") == "text").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def _load_done() -> Dict[str, set]:
    done: Dict[str, set] = {"node": set(), "community": set(), "edge": set()}
    if not config.ENRICH_LOG.exists():
        return done
    for line in config.ENRICH_LOG.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("kind") in done:
            done[rec["kind"]].add(str(rec.get("key")))
    return done


def load_enrichment() -> Dict[str, Dict[str, dict]]:
    out: Dict[str, Dict[str, dict]] = {"node": {}, "community": {}, "edge": {}}
    if not config.ENRICH_LOG.exists():
        return out
    for line in config.ENRICH_LOG.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("kind") in out:
            out[rec["kind"]][str(rec["key"])] = rec.get("data") or {}
    return out


def _node_context(node: dict, max_chars: int = config.MAX_CONTEXT_CHARS) -> str:
    """Highest-signal pages of a node's source, sent once per node."""
    keys = keywords(node.get("label", ""))
    for source_file in node_sources(node):
        src = _load_source(source_file)
        if not src:
            continue
        text, pages = src["text"], src["pages"]
        if not keys:
            return text[:max_chars]
        scored = sorted(
            ((sum(p.body.lower().count(k) for k in keys), p.body) for p in pages),
            key=lambda x: -x[0],
        )
        buf, size = [], 0
        for score, body in scored:
            if not score:
                break
            chunk = body[:1800]
            if size + len(chunk) > max_chars:
                break
            buf.append(chunk)
            size += len(chunk)
        if buf:
            return "\n\n----\n\n".join(buf)
        return text[:max_chars]
    return "(source not found)"


def _batched(items: Sequence, size: int) -> Iterable[list]:
    for i in range(0, len(items), size):
        yield list(items[i:i + size])


def _run_batches(name: str, batches: List[list], worker: Callable[[list], None]) -> None:
    if not batches:
        print(f"{name}: nothing to do")
        return
    print(f"{name}: {len(batches)} batches across {config.ENRICH_WORKERS} workers")
    done = 0
    lock = threading.Lock()

    def _wrapped(batch):
        nonlocal done
        try:
            worker(batch)
        except Exception as exc:  # a failed batch must not kill the stage
            print(f"    BATCH FAILED ({exc.__class__.__name__}): {exc}", flush=True)
        with lock:
            done += 1
            if done % 5 == 0 or done == len(batches):
                print(f"    {name}: {done}/{len(batches)} batches", flush=True)

    with ThreadPoolExecutor(max_workers=config.ENRICH_WORKERS) as pool:
        list(pool.map(_wrapped, batches))


def select_narrative_edges(nodes: Dict[str, dict], links: List[dict]) -> List[dict]:
    """Edges that earn a written narrative.

    Every edge already carries a verbatim excerpt and an exact page from the
    free grounding pass, so a narrative is an extra that has to justify itself:
    it goes to links that cross regimes, links the reader cannot take at face
    value, and links on the hubs everything routes through.
    """
    deg = degrees(links)
    picked = []
    for e in links:
        a, b = nodes.get(e["source"]), nodes.get(e["target"])
        if not a or not b:
            continue
        conf = (e.get("confidence") or "").upper()
        cross = (config.EDGE_NARRATIVE_CROSS_COMMUNITY
                 and a.get("community") is not None
                 and a.get("community") != b.get("community"))
        low = conf in config.EDGE_NARRATIVE_LOW_CONFIDENCE
        hub = max(deg[e["source"]], deg[e["target"]]) >= config.EDGE_NARRATIVE_HUB_DEGREE
        if cross or low or hub:
            score = (3 if cross else 0) + (2 if low else 0) + (1 if hub else 0)
            picked.append((score, e))
    picked.sort(key=lambda x: -x[0])
    return [e for _, e in picked[:config.EDGE_NARRATIVE_MAX]]


def enrich(nodes: Dict[str, dict], links: List[dict], grounding: dict,
           limit_nodes: Optional[int] = None, skip_edges: bool = False) -> None:
    api_key = config.enrich_api_key()
    done = _load_done()
    key_src = (config.ENRICH_KEY_ENV if os.environ.get(config.ENRICH_KEY_ENV, "").strip()
               else "ANTHROPIC_API_KEY")
    print(f"Model: {config.ENRICH_MODEL}  (key from {key_src})")

    # --- per-node summaries ------------------------------------------------ #
    todo_nodes = [n for nid, n in nodes.items() if nid not in done["node"]]
    if limit_nodes:
        todo_nodes = todo_nodes[:limit_nodes]
    print(f"Nodes: {len(nodes)} total, {len(nodes) - len(todo_nodes)} already done, "
          f"{len(todo_nodes)} to enrich")

    def node_worker(batch: List[dict]) -> None:
        payload = {"nodes": [{
            "id": n["id"], "label": n.get("label"),
            "sources": [stem_of_source(s) for s in node_sources(n)],
            "context": _node_context(n),
        } for n in batch]}
        res = claude_json(SYS_NODES, json.dumps(payload, ensure_ascii=False), api_key)
        got = {str(i.get("id")) for i in res.get("nodes", [])}
        for item in res.get("nodes", []):
            _append_jsonl(config.ENRICH_LOG,
                          {"kind": "node", "key": str(item.get("id")), "data": item})
        for n in batch:
            if n["id"] not in got:
                print(f"    node missing from response: {n.get('label')}", flush=True)

    _run_batches("nodes", list(_batched(todo_nodes, config.NODE_BATCH)), node_worker)

    # --- communities ------------------------------------------------------- #
    members: Dict[Any, List[str]] = defaultdict(list)
    names: Dict[Any, str] = {}
    for nid, n in nodes.items():
        cid = n.get("community")
        if cid is None:
            continue
        members[cid].append(nid)
        if n.get("community_name"):
            names[cid] = n["community_name"]

    todo_comms = [cid for cid in members if str(cid) not in done["community"]]
    print(f"Communities: {len(members)} total, {len(todo_comms)} to enrich")

    def comm_worker(batch: List[Any]) -> None:
        items = []
        for cid in batch:
            mset = set(members[cid])
            internal = [{"a": nodes[l["source"]].get("label"),
                         "b": nodes[l["target"]].get("label"),
                         "relation": l.get("relation")}
                        for l in links if l["source"] in mset and l["target"] in mset][:20]
            items.append({"community_id": cid, "name": names.get(cid, f"Community {cid}"),
                          "members": [nodes[m].get("label", m) for m in members[cid]],
                          "internal_edges_sample": internal})
        res = claude_json(SYS_COMMUNITIES, json.dumps({"communities": items}, ensure_ascii=False),
                          api_key)
        for item in res.get("communities", []):
            _append_jsonl(config.ENRICH_LOG,
                          {"kind": "community", "key": str(item.get("community_id")), "data": item})

    _run_batches("communities", list(_batched(todo_comms, config.COMMUNITY_BATCH)), comm_worker)

    # --- selected edge narratives ------------------------------------------ #
    if skip_edges:
        print("Edge narratives: skipped")
        return
    selected = select_narrative_edges(nodes, links)
    todo_edges = [e for e in selected if edge_key(e) not in done["edge"]]
    print(f"Edge narratives: {len(selected)} selected of {len(links)} edges "
          f"({len(todo_edges)} to enrich)")

    def edge_worker(batch: List[dict]) -> None:
        items = []
        for e in batch:
            ia, ib = sorted([e["source"], e["target"]])
            g = grounding.get(edge_key(e)) or {}
            items.append({
                "edge_key": edge_key(e),
                "relation": e.get("relation"), "confidence": e.get("confidence"),
                "node_a": {"label": nodes[ia].get("label"),
                           "excerpt": (g.get("clause_a") or {}).get("excerpt")},
                "node_b": {"label": nodes[ib].get("label"),
                           "excerpt": (g.get("clause_b") or {}).get("excerpt")},
            })
        res = claude_json(SYS_EDGES, json.dumps({"edges": items}, ensure_ascii=False), api_key)
        for item in res.get("edges", []):
            _append_jsonl(config.ENRICH_LOG,
                          {"kind": "edge", "key": str(item.get("edge_key")), "data": item})

    _run_batches("edges", list(_batched(todo_edges, config.EDGE_BATCH)), edge_worker)
    report_usage()


def report_usage() -> None:
    if not config.USAGE_LOG.exists():
        return
    tot_in = tot_cached = tot_out = 0
    cost = 0.0
    calls = 0
    for line in config.USAGE_LOG.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except json.JSONDecodeError:
            continue
        calls += 1
        tot_in += r.get("input_tokens", 0)
        tot_cached += r.get("cache_read_input_tokens", 0)
        tot_out += r.get("output_tokens", 0)
        cost += r.get("est_cost_usd", 0.0)
    print(f"\nUsage ledger ({calls} calls): input={tot_in:,} cached={tot_cached:,} "
          f"output={tot_out:,} | est ${cost:,.2f}  -> {config.USAGE_LOG}")


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

def _clause_line(title: str, clause: Optional[dict]) -> str:
    if not clause or not clause.get("excerpt"):
        return f"- **{title}:** _(no supporting sentence located — open the source)_"
    ex = strip_presentation_forms(clause["excerpt"])
    stem = stem_of_source(clause.get("source_file"))
    loc = f"{stem} · Page {clause['page']}" if clause.get("page") else stem
    return f"- **{title}** ({loc}): \"{ex}\""


def render(nodes: Dict[str, dict], links: List[dict], grounding: dict) -> Tuple[int, int]:
    enr = load_enrichment()
    incident: Dict[str, List[dict]] = defaultdict(list)
    for l in links:
        incident[l["source"]].append(l)
        incident[l["target"]].append(l)

    by_label: Dict[str, Path] = {}
    for p in config.VAULT_DIR.glob("*.md"):
        if not p.name.startswith("_COMMUNITY_"):
            by_label[p.stem] = p

    def find_note(label: str) -> Optional[Path]:
        from .common import strip_forbidden
        direct = config.VAULT_DIR / f"{strip_forbidden(label)}.md"
        if direct.exists():
            return direct
        return by_label.get(strip_forbidden(label))

    written = 0
    for nid, node in nodes.items():
        label = node.get("label") or nid
        path = find_note(label)
        if not path:
            continue

        summary = enr["node"].get(str(nid)) or {}
        lines = [f"# {label}", ""]
        if summary.get("summary"):
            lines += [summary["summary"], ""]
        if summary.get("regimes"):
            lines += [f"**Regimes:** {', '.join(summary['regimes'])}", ""]

        srcs = node_sources(node)
        if srcs:
            lines += ["## Sources", ""]
            lines += [f"- `corpus/markdown/{Path(s).name}`" for s in srcs]
            lines.append("")

        edges = incident.get(nid, [])
        if edges:
            lines += ["## Connections", ""]
            for e in sorted(edges, key=lambda x: (nodes.get(
                    x["target"] if x["source"] == nid else x["source"], {}).get("label") or "")):
                other_id = e["target"] if e["source"] == nid else e["source"]
                other = nodes.get(other_id)
                if not other:
                    continue
                ek = edge_key(e)
                g = grounding.get(ek) or {}
                ia, _ib, _rel = ek.split("||", 2)
                mine = g.get("clause_a") if nid == ia else g.get("clause_b")
                theirs = g.get("clause_b") if nid == ia else g.get("clause_a")

                lines.append(f"### {wikilink(other.get('label', other_id))} — "
                             f"`{e.get('relation', '')}` [{e.get('confidence', 'EXTRACTED')}]")
                narrative = (enr["edge"].get(ek) or {}).get("why")
                if narrative:
                    lines.append(f"- **What this link tells you:** {narrative}")
                lines.append(_clause_line("Grounding — this node", mine))
                lines.append(_clause_line("Grounding — related node", theirs))
                if g.get("caveat"):
                    lines.append(f"- **Caveat:** {g['caveat']}")
                lines.append("")

        if summary.get("lookup_terms"):
            lines += ["## Lookup terms", "",
                      ", ".join(f"`{t}`" for t in summary["lookup_terms"]), ""]

        tags = ["#graphify/enriched"]
        if node.get("community_name"):
            tags.append("#community/"
                        + re.sub(r"\s+", "-", str(node["community_name"]).lower()))
        lines.append(" ".join(tags))

        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written += 1

    # community notes
    comm_written = 0
    names: Dict[Any, str] = {}
    members: Dict[Any, List[str]] = defaultdict(list)
    for nid, n in nodes.items():
        cid = n.get("community")
        if cid is None:
            continue
        members[cid].append(n.get("label", nid))
        if n.get("community_name"):
            names[cid] = n["community_name"]

    for cid, name in names.items():
        data = enr["community"].get(str(cid))
        path = config.VAULT_DIR / f"_COMMUNITY_{name}.md"
        if not path.exists():
            matches = [p for p in config.VAULT_DIR.glob("_COMMUNITY_*.md") if name in p.stem]
            if not matches:
                continue
            path = matches[0]
        lines = [f"# {name}", ""]
        if data:
            if data.get("theme"):
                lines += ["## Why this community", "", data["theme"], ""]
            if data.get("how_members_connect"):
                lines += ["## How members connect", ""]
                lines += [f"- {str(b).lstrip('- ').strip()}" for b in data["how_members_connect"]]
                lines.append("")
            if data.get("start_here"):
                lines += ["## Start here", ""]
                lines += [f"- {wikilink(str(m))}" for m in data["start_here"]]
                lines.append("")
        lines += ["## Members", ""]
        lines += [f"- {wikilink(m)}" for m in sorted(members[cid])]
        slug = re.sub(r"\\s+", "-", str(name).lower())
        lines += ["", f"#community/{slug}"]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        comm_written += 1

    print(f"Rendered {written} node notes, {comm_written} community notes")
    return written, comm_written


# --------------------------------------------------------------------------- #
# Routing index
# --------------------------------------------------------------------------- #

def routing_index(nodes: Dict[str, dict], links: List[dict]) -> Path:
    """The vault's own index page for a human reader opening it in Obsidian.

    README.md tells a person to "start at _INDEX_Routing.md" - this writes that
    file: term -> node -> source stem -> page, all as wikilinks into the vault.
    """
    enr = load_enrichment()
    deg = degrees(links)

    by_regime: Dict[str, List[str]] = defaultdict(list)
    term_rows: List[Tuple[str, str, str]] = []
    stem_rows: Dict[str, List[str]] = defaultdict(list)

    for nid, n in nodes.items():
        label = n.get("label") or nid
        data = enr["node"].get(str(nid)) or {}
        for r in data.get("regimes") or []:
            by_regime[str(r)].append(label)
        stems = [stem_of_source(s) for s in node_sources(n)]
        for s in stems:
            stem_rows[s].append(label)
        for t in (data.get("lookup_terms") or [])[:8]:
            term_rows.append((str(t), label, ", ".join(f"`{s}`" for s in stems[:3])))

    communities: Dict[Any, dict] = {}
    for nid, n in nodes.items():
        cid = n.get("community")
        if cid is not None and cid not in communities:
            communities[cid] = {"name": n.get("community_name") or f"Community {cid}",
                                "members": []}
        if cid is not None:
            communities[cid]["members"].append(n.get("label", nid))

    lines = [
        "# Routing index", "",
        "> Generated by the pipeline — do not edit by hand.",
        "> Use this to go from a question to the stems worth opening. "
        "**Corpus text wins**: always verify in `corpus/markdown/`.", "",
        "## By regime", "",
    ]
    for regime in sorted(by_regime):
        lines.append(f"### {regime}")
        lines.append("")
        lines += [f"- {wikilink(m)}" for m in sorted(set(by_regime[regime]))[:60]]
        lines.append("")

    lines += ["## By community", "",
              md_table(["Community", "Members", "Start here"],
                       [[c["name"], len(c["members"]),
                         ", ".join((enr["community"].get(str(cid)) or {}).get("start_here") or [])]
                        for cid, c in sorted(communities.items(), key=lambda x: str(x[1]["name"]))]),
              ""]

    lines += ["## Hubs", "",
              md_table(["Node", "Degree", "Sources"],
                       [[nodes[nid].get("label"), d,
                         ", ".join(f"`{stem_of_source(s)}`" for s in node_sources(nodes[nid])[:3])]
                        for nid, d in sorted(deg.items(), key=lambda x: -x[1])[:25]
                        if nid in nodes]),
              ""]

    lines += ["## Lookup terms", "",
              md_table(["Term", "Node", "Stems"],
                       sorted(set(term_rows))[:1500]), ""]

    lines += ["## By source document", "",
              md_table(["Stem", "Nodes"],
                       [[f"`{s}`", ", ".join(sorted(set(v))[:12])]
                        for s, v in sorted(stem_rows.items())]), ""]

    out = config.VAULT_DIR / "_INDEX_Routing.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Routing index -> {out}")
    return out


# --------------------------------------------------------------------------- #

def run(skip_model: bool = False, skip_edges: bool = False,
        limit_nodes: Optional[int] = None, apply_only: bool = False) -> int:
    utf8_console()
    config.ensure_dirs()
    if not config.VAULT_DIR.exists() or not list(config.VAULT_DIR.glob("*.md")):
        print(f"Vault {config.VAULT_DIR} is empty — run the build stage first.")
        return 1

    nodes, links = load_graph()

    if apply_only:
        grounding = (read_json(config.GROUNDING_JSON) or {}).get("grounding") or {}
    else:
        print("\n--- grounding (deterministic, no tokens) ---")
        grounding = ground(nodes, links)

    if not skip_model and not apply_only:
        print("\n--- enrichment (model) ---")
        enrich(nodes, links, grounding, limit_nodes=limit_nodes, skip_edges=skip_edges)

    print("\n--- rendering ---")
    render(nodes, links, grounding)
    routing_index(nodes, links)
    return 0
