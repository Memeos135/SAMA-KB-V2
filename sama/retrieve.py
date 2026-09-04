"""Query-time retrieval for the v2 agent workflow.  No tokens, no model.

The v1 workflow answered "where do I look" by fanning out a wave of model
agents to grep 379 corpus files.  That question was already answered offline:
the enrich stage wrote lookup terms, regimes, communities and page-exact
grounding, and the routing index turned them into a lookup table.  This module
reads those artifacts and returns the shortlist directly, so the model's budget
goes on reading law rather than finding it.

The tuning is asymmetric on purpose.  A stem that is retrieved and discarded
costs one page read; a stem that is never retrieved is a silent hole in the
answer.  So direct term hits are treated as entry points, not as the answer
set, and the result is widened along communities and graph neighbours before
it is returned.

Misses are first-class output.  A facet with no index hit is not a facet with
no law - the index is derived from the graph, so anything the extractor never
turned into a node is invisible here.  Those facets are reported explicitly and
are the one case that still requires a corpus grep.

    python -m sama.retrieve "beneficial owner verification"
    python -m sama.retrieve --facet "CDD" --facet "reliance on third parties"
    python -m sama.retrieve "APR cap" --regime BNPL/finance --json
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Set, Tuple

from . import config
from .common import (
    md_table, parse_md_pages, read_json, resolve_source, stem_for, stem_of_source,
    utf8_console,
)
from .enrich import degrees, load_enrichment, load_graph, node_sources

# Terms that carry no routing signal in a corpus where every document is a SAMA
# instrument.  Kept separate from common._STOPWORDS, which tunes label keywords.
_QUERY_STOP = {
    "a", "an", "and", "any", "are", "as", "at", "be", "by", "can", "do", "does",
    "for", "from", "has", "have", "how", "in", "is", "it", "its", "may", "must",
    "of", "on", "or", "our", "shall", "should", "that", "the", "their", "them",
    "there", "these", "this", "to", "under", "was", "were", "what", "when",
    "where", "which", "who", "why", "will", "with", "would",
    "sama", "saudi", "rule", "rules", "regulation", "regulations", "requirement",
    "requirements", "law", "laws", "circular", "circulars",
}

_WORD_RE = re.compile(r"[0-9A-Za-z\u0600-\u06FF\u0750-\u077F]+")


def _tokens(text: str) -> List[str]:
    return [t for t in _WORD_RE.findall((text or "").lower()) if t not in _QUERY_STOP]


def _phrase(text: str) -> str:
    return " ".join(_WORD_RE.findall((text or "").lower()))


# --------------------------------------------------------------------------- #
# Index
# --------------------------------------------------------------------------- #

class Index:
    """Everything the pipeline already knows about where text lives.

    Built once per process from graph.json, the enrichment log and
    grounding.json.  Nothing here is inferred at query time.
    """

    def __init__(self) -> None:
        self.nodes, self.links = load_graph()
        enr = load_enrichment()
        self.degree = degrees(self.links)

        self.meta: Dict[str, dict] = {}
        self.blob: Dict[str, dict] = {}
        self.stems: Dict[str, List[str]] = {}

        for nid, n in self.nodes.items():
            data = enr["node"].get(str(nid)) or {}
            label = n.get("label") or nid
            lookup = [str(t) for t in (data.get("lookup_terms") or [])]
            regimes = [str(r) for r in (data.get("regimes") or [])]
            stems = [s for s in (stem_of_source(s) for s in node_sources(n)) if s]

            self.stems[nid] = stems
            self.meta[nid] = {
                "label": label,
                "regimes": regimes,
                "community": n.get("community_name"),
                "summary": str(data.get("summary") or ""),
                "sources": node_sources(n),
            }
            self.blob[nid] = {
                "label": _phrase(label),
                "label_tokens": set(_tokens(label)),
                "lookup": [_phrase(t) for t in lookup],
                "lookup_tokens": set(_tokens(" ".join(lookup))),
                "regimes": {_phrase(r) for r in regimes},
                "community": _phrase(n.get("community_name") or ""),
                "summary_tokens": set(_tokens(str(data.get("summary") or ""))),
            }

        self.community: Dict[str, List[str]] = defaultdict(list)
        for nid, n in self.nodes.items():
            cid = n.get("community")
            if cid is not None:
                self.community[str(cid)].append(nid)
        self.community_of = {
            nid: str(n["community"])
            for nid, n in self.nodes.items()
            if n.get("community") is not None
        }

        self.neighbours: Dict[str, Set[str]] = defaultdict(set)
        for l in self.links:
            self.neighbours[l["source"]].add(l["target"])
            self.neighbours[l["target"]].add(l["source"])

        self.anchors = self._page_anchors()

    def _page_anchors(self) -> Dict[str, Dict[Tuple[str, int], str]]:
        """node -> {(stem, page): excerpt}, straight out of the grounding pass.

        These pages are where a sentence supporting this node was actually
        found, with the page derived from a byte offset - so they are exact,
        and they let a digger open a page instead of a 1.9 MB file.
        """
        raw = (read_json(config.GROUNDING_JSON) or {}).get("grounding") or {}
        out: Dict[str, Dict[Tuple[str, int], str]] = defaultdict(dict)
        for ek, g in raw.items():
            parts = ek.split("||", 2)
            if len(parts) < 2:
                continue
            for nid, clause in ((parts[0], g.get("clause_a")), (parts[1], g.get("clause_b"))):
                if not clause or not clause.get("page"):
                    continue
                stem = stem_of_source(clause.get("source_file"))
                if stem:
                    out[nid].setdefault((stem, int(clause["page"])), clause.get("excerpt") or "")
        return out

    def rel_path(self, stem: str) -> str:
        for nid, stems in self.stems.items():
            if stem in stems:
                for src in self.meta[nid]["sources"]:
                    if stem_of_source(src) == stem:
                        path = resolve_source(src)
                        if path:
                            return path.relative_to(config.ROOT).as_posix()
        return f"corpus/markdown/{stem}.md"


# --------------------------------------------------------------------------- #
# Corpus scan
#
# The graph cannot be the only way in.  Grounding only covers nodes that ended
# up on an edge, and the index only covers concepts the extractor turned into a
# node - so two holes are possible: a shortlisted stem with no page anchors, and
# a facet with no node at all.  Both are closed here by scanning the text
# directly.  It is a script reading files, so it is cheap enough to be
# unconditional, and it means a hole is never left for the model to notice.
# --------------------------------------------------------------------------- #

_pages_cache: Dict[str, List[Tuple[int, str]]] = {}


def _pages_of(path) -> List[Tuple[int, str]]:
    key = str(path)
    if key not in _pages_cache:
        text = path.read_text(encoding="utf-8", errors="replace")
        _pages_cache[key] = [(p.number, p.body.lower()) for p in parse_md_pages(text)]
    return _pages_cache[key]


def page_hits(path, tokens: Sequence[str], limit: int) -> List[int]:
    """Pages of one document ranked by how many facet tokens they carry."""
    if not tokens:
        return []
    scored: List[Tuple[int, int]] = []
    for number, body in _pages_of(path):
        hits = sum(1 for t in set(tokens) if t in body)
        if hits:
            scored.append((hits, number))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [n for _h, n in scored[:limit]]


def scan_corpus(facets: Sequence[str], limit_stems: int = 8) -> Dict[str, dict]:
    """Full-text fallback for facets the index never heard of.

    Every facet token must appear on the page, so this is a conjunctive search:
    a facet that survives it is genuinely in the corpus, and a facet that does
    not is a defensible NOT_FOUND_IN_CONTEXT rather than a retrieval failure.
    """
    out: Dict[str, dict] = {}
    for facet in facets:
        tokens = _tokens(facet)
        if not tokens:
            out[facet] = {}
            continue
        found: Dict[str, List[int]] = {}
        for path in sorted(config.CORPUS_MD.glob("*.md")):
            pages = [n for n, body in _pages_of(path)
                     if all(t in body for t in tokens)]
            if pages:
                found[stem_for(path.name)] = pages[:config.RETRIEVE_MAX_PAGES_PER_STEM]
        out[facet] = dict(sorted(found.items(), key=lambda kv: -len(kv[1]))[:limit_stems])
    return out


# --------------------------------------------------------------------------- #
# Scoring
# --------------------------------------------------------------------------- #

def _phrase_match(a: str, b: str, min_tokens: int = 2) -> bool:
    """One phrase contains the other, and the contained side means something.

    Bare containment makes every one-word label a hit on any facet mentioning
    that word - "Regular Insurance" matches "unicorn insurance for spaceships" -
    which is how a facet with no real coverage ends up looking answered.
    """
    if not a or not b:
        return False
    short, long = (a, b) if len(a) <= len(b) else (b, a)
    if len(short.split()) < min_tokens:
        return False
    return f" {short} " in f" {long} "


def score_node(blob: dict, facet_phrase: str, facet_tokens: Sequence[str]) -> float:
    """How strongly one node answers to one facet.

    Lookup terms outrank the label because they were written to be searched;
    the summary contributes only enough to break ties, since it is model prose
    and never authority.

    A phrase match short-circuits the coverage gate.  Otherwise the node has to
    carry RETRIEVE_MIN_COVERAGE of the facet's tokens somewhere - without that,
    one incidental shared word scores an unrelated node as a hit, and a facet
    that should have been reported as NOT_FOUND_IN_CONTEXT silently looks
    answered.
    """
    if not facet_tokens:
        return 0.0
    tok = set(facet_tokens)
    score = 0.0

    for term in blob["lookup"]:
        if _phrase_match(term, facet_phrase):
            score += 5.0
            break
    if _phrase_match(blob["label"], facet_phrase):
        score += 4.0

    matched = tok & (blob["lookup_tokens"] | blob["label_tokens"] | blob["summary_tokens"])
    if score == 0.0 and len(matched) / len(tok) < config.RETRIEVE_MIN_COVERAGE:
        return 0.0

    score += 2.0 * len(tok & blob["lookup_tokens"]) / len(tok)
    score += 1.5 * len(tok & blob["label_tokens"]) / len(tok)
    score += 0.5 * len(tok & blob["summary_tokens"]) / len(tok)
    if blob["community"] and tok & set(blob["community"].split()):
        score += 0.5
    return score


def retrieve(facets: Sequence[str], regime: Optional[str] = None,
             k: int = config.RETRIEVE_K, index: Optional[Index] = None) -> dict:
    idx = index or Index()

    scored: Dict[str, float] = defaultdict(float)
    hit_facets: Dict[str, Set[str]] = defaultdict(set)
    facet_rows: List[dict] = []
    misses: List[str] = []

    want_regime = _phrase(regime) if regime else None

    for facet in facets:
        phrase, tokens = _phrase(facet), _tokens(facet)
        hits = 0
        for nid, blob in idx.blob.items():
            if want_regime and want_regime not in blob["regimes"]:
                continue
            s = score_node(blob, phrase, tokens)
            if s < config.RETRIEVE_MIN_SCORE:
                continue
            scored[nid] += s
            hit_facets[nid].add(facet)
            hits += 1
        facet_rows.append({"facet": facet, "nodes": hits,
                           "status": "HIT" if hits else "MISS"})
        if not hits:
            misses.append(facet)

    seeds = sorted(scored, key=lambda n: -scored[n])[:k]
    expanded = _expand(idx, seeds, scored, hit_facets)

    ranked = sorted(set(seeds) | expanded, key=lambda n: -scored[n])[:k + config.RETRIEVE_EXPAND_MAX]

    nodes_out, by_stem = _shape(idx, ranked, scored, hit_facets)

    recovered: Dict[str, dict] = {}
    if misses:
        for facet, found in scan_corpus(misses).items():
            if not found:
                continue
            recovered[facet] = found
            for stem, pages in found.items():
                row = by_stem.setdefault(stem, {
                    "path": idx.rel_path(stem), "pages": [], "nodes": [], "score": 0.0,
                })
                row["pages"] = sorted(set(row["pages"]) | set(pages))
                row["via"] = "corpus-scan"
                row["nodes"] = sorted(set(row["nodes"]) | {f"(scan: {facet})"})

    _resolve_pages(by_stem, [t for f in facets for t in _tokens(f)])

    not_found = [m for m in misses if m not in recovered]
    for row in facet_rows:
        if row["facet"] in recovered:
            row["status"] = "SCAN"
            row["nodes"] = sum(len(v) for v in recovered[row["facet"]].values())
        elif row["facet"] in not_found:
            row["status"] = "NOT_FOUND_IN_CONTEXT"

    by_stem = dict(sorted(by_stem.items(), key=lambda kv: -kv[1]["score"]))
    return {
        "query": " | ".join(facets),
        "regime": regime,
        "facets": facet_rows,
        "recovered_by_scan": recovered,
        "not_found": not_found,
        "nodes": nodes_out,
        "by_stem": by_stem,
        "dig_plan": plan_diggers(by_stem),
        "stats": {
            "seeds": len(seeds),
            "expanded": len(expanded),
            "stems": len(by_stem),
            "graph_nodes": len(idx.nodes),
        },
    }


def _resolve_pages(by_stem: Dict[str, dict], facet_tokens: Sequence[str]) -> None:
    """Give every stem a concrete page list, or take it off the dig plan.

    Grounding only covers nodes that landed on an edge, and a node's lookup
    terms are model prose that need not appear in its own source - so a
    shortlisted stem can arrive with no pages at all.  "Open the whole
    document" is not an acceptable brief for a 902-page instrument, so the text
    is scanned for the facet, then for the node's own label.  What still has no
    page signal is reported to Counsel but left unscheduled: visible, and not
    something a digger will pull into context on a hunch.
    """
    for row in by_stem.values():
        path = config.ROOT / row["path"]
        row["doc_pages"] = len(_pages_of(path)) if path.exists() else 0
        row["scheduled"] = True

        if row["pages"] or not path.exists():
            continue

        for tokens, via in ((facet_tokens, "page-scan"),
                            (_tokens(" ".join(row["nodes"])), "label-scan")):
            found = page_hits(path, tokens, config.RETRIEVE_MAX_PAGES_PER_STEM)
            if found:
                row["pages"], row["via"] = sorted(found), via
                break
        else:
            if 0 < row["doc_pages"] <= config.RETRIEVE_SMALL_DOC_PAGES:
                row["pages"] = list(range(1, row["doc_pages"] + 1))
                row["via"] = "small-doc"
            else:
                row["scheduled"] = False
                row["via"] = "no-page-signal"


def _expand(idx: Index, seeds: Sequence[str], scored: Dict[str, float],
            hit_facets: Dict[str, Set[str]]) -> Set[str]:
    """Pull in the neighbourhood of every seed.

    A question names a concept; the obligation that answers it often sits on the
    instrument next to that concept.  Expansion is what stops the answer from
    being only as good as the user's vocabulary.
    """
    out: Set[str] = set()
    if not (config.RETRIEVE_EXPAND_COMMUNITY or config.RETRIEVE_EXPAND_NEIGHBOURS):
        return out

    for seed in seeds:
        if len(out) >= config.RETRIEVE_EXPAND_MAX:
            break
        pool: Set[str] = set()
        if config.RETRIEVE_EXPAND_NEIGHBOURS:
            pool |= idx.neighbours.get(seed, set())
        if config.RETRIEVE_EXPAND_COMMUNITY:
            cid = idx.community_of.get(seed)
            if cid:
                pool |= set(idx.community[cid])
        for nid in pool:
            if nid in scored or nid not in idx.nodes:
                continue
            scored[nid] = scored[seed] * config.RETRIEVE_EXPAND_DECAY
            hit_facets[nid] |= {f"~{f}" for f in hit_facets.get(seed, set())}
            out.add(nid)
            if len(out) >= config.RETRIEVE_EXPAND_MAX:
                break
    return out


def _shape(idx: Index, ranked: Sequence[str], scored: Dict[str, float],
           hit_facets: Dict[str, Set[str]]) -> Tuple[List[dict], Dict[str, dict]]:
    nodes_out: List[dict] = []
    by_stem: Dict[str, dict] = {}

    for nid in ranked:
        meta = idx.meta[nid]
        anchors = idx.anchors.get(nid, {})
        pages = sorted({p for _s, p in anchors})[:config.RETRIEVE_MAX_PAGES_PER_STEM]
        snippet = next(iter(anchors.values()), "")[:config.RETRIEVE_SNIPPET_CHARS]

        nodes_out.append({
            "node": meta["label"],
            "score": round(scored[nid], 2),
            "via": sorted(hit_facets.get(nid, set())),
            "regimes": meta["regimes"],
            "community": meta["community"],
            "degree": idx.degree.get(nid, 0),
            "stems": idx.stems[nid],
            "pages": pages,
            "snippet": snippet,
        })

        for stem in idx.stems[nid]:
            row = by_stem.setdefault(stem, {
                "path": idx.rel_path(stem), "pages": set(), "nodes": [], "score": 0.0,
            })
            row["nodes"].append(meta["label"])
            row["score"] = max(row["score"], round(scored[nid], 2))
            row["pages"] |= {p for s, p in anchors if s == stem}

    for row in by_stem.values():
        row["pages"] = sorted(row["pages"])[:config.RETRIEVE_MAX_PAGES_PER_STEM]
        row["nodes"] = sorted(set(row["nodes"]))
    return nodes_out, dict(sorted(by_stem.items(), key=lambda kv: -kv[1]["score"]))


def plan_diggers(by_stem: Dict[str, dict]) -> List[dict]:
    """Pack stems into balanced dig briefs, always at least one.

    Fan-out is arithmetic, not judgement.  There is no "counsel reads this one
    itself" shortcut: counsel has no corpus access at all, so every page of
    text in the final answer arrives through a digger.  Stems are dealt into
    buckets by page count, so no digger is handed the 902-page instrument plus
    five others.
    """
    def brief(stem: str) -> dict:
        row = by_stem[stem]
        return {"stem": stem, "path": row["path"], "pages": row["pages"],
                "doc_pages": row.get("doc_pages", 0)}

    def weight(stem: str) -> int:
        row = by_stem[stem]
        return max(1, len(row["pages"]) or row.get("doc_pages", 1))

    stems = [s for s, row in by_stem.items() if row.get("scheduled", True)]
    if not stems:
        return []

    buckets: List[dict] = [{"digger": i + 1, "weight": 0, "stems": []}
                           for i in range(min(config.DIGGER_MAX, len(stems)))]
    for stem in sorted(stems, key=lambda s: -weight(s)):
        b = min(buckets, key=lambda x: x["weight"])
        b["stems"].append(brief(stem))
        b["weight"] += weight(stem)
    return [b for b in buckets if b["stems"]]


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def _render(res: dict) -> str:
    out = [f"# Retrieval — {res['query']}", ""]
    if res["regime"]:
        out += [f"Regime filter: `{res['regime']}`", ""]

    out += ["## Facets", "",
            md_table(["Facet", "Nodes", "Status"],
                     [[r["facet"], r["nodes"], r["status"]] for r in res["facets"]]), ""]

    if res["recovered_by_scan"]:
        out += ["## Recovered by corpus scan", "",
                "No graph node carried these facets, so the corpus text was searched "
                "directly. Treat them as first-class — the graph simply never extracted "
                "them.", ""]
        for facet, found in res["recovered_by_scan"].items():
            stems = ", ".join(f"`{s}` p.{','.join(str(p) for p in pp[:4])}"
                              for s, pp in found.items())
            out.append(f"- **{facet}** — {stems}")
        out.append("")

    if res["not_found"]:
        out += ["## NOT_FOUND_IN_CONTEXT", "",
                "Absent from the index *and* from a conjunctive full-text scan of "
                "`corpus/markdown/`. Say so explicitly in the answer; do not quietly "
                "drop the facet.", ""]
        out += [f"- `{m}`" for m in res["not_found"]]
        out.append("")

    scheduled = {s: r for s, r in res["by_stem"].items() if r.get("scheduled", True)}
    unscheduled = {s: r for s, r in res["by_stem"].items() if not r.get("scheduled", True)}

    out += ["## Stems to open", "",
            md_table(["Stem", "Pages", "Doc", "Score", "Nodes", "Via"],
                     [[f"`{s}`", ", ".join(str(p) for p in r["pages"]),
                       f"{r.get('doc_pages', 0)}p", r["score"], len(r["nodes"]),
                       r.get("via", "index")]
                      for s, r in scheduled.items()]), ""]

    if unscheduled:
        out += ["## Surfaced but not scheduled", "",
                "These stems relate to the question but carry no page-level signal for "
                "it, and they are too large to open blind. Not in the dig plan. Schedule "
                "one explicitly only if the answer turns out to need it.", "",
                md_table(["Stem", "Doc", "Score", "Nodes"],
                         [[f"`{s}`", f"{r.get('doc_pages', 0)}p", r["score"],
                           ", ".join(r["nodes"][:3])]
                          for s, r in unscheduled.items()]), ""]

    shown = res["nodes"][:config.RETRIEVE_RENDER_NODES]
    out += ["## Nodes", "",
            md_table(["Node", "Score", "Regimes", "Community", "Stems", "Pages"],
                     [[n["node"], n["score"], ", ".join(n["regimes"]), n["community"] or "",
                       ", ".join(f"`{s}`" for s in n["stems"]),
                       ", ".join(str(p) for p in n["pages"])]
                      for n in shown]), ""]
    if len(res["nodes"]) > len(shown):
        out += [f"_{len(res['nodes']) - len(shown)} lower-scoring nodes omitted from this "
                f"table; their stems are all listed above and `--json` returns every one._", ""]

    out += ["## Dig plan", "",
            "One Task per digger, all in one turn. Every brief names explicit pages — "
            "there is no 'open the whole document' brief, and no lane where counsel "
            "reads the corpus itself.", ""]
    for b in res["dig_plan"]:
        for s in b["stems"]:
            out.append(f"- **digger {b['digger']}** — `{s['path']}` pages "
                       f"{', '.join(str(p) for p in s['pages'])}")
    out += ["", f"_{len(scheduled)} stems scheduled"
                + (f", {len(unscheduled)} surfaced but unscheduled" if unscheduled else "")
                + f", from {res['stats']['seeds']} seed nodes + {res['stats']['expanded']} "
                  f"expanded, out of {res['stats']['graph_nodes']} in the graph._"]
    return "\n".join(out)


def main(argv: Optional[Sequence[str]] = None) -> int:
    utf8_console()
    ap = argparse.ArgumentParser(
        prog="python -m sama.retrieve",
        description="Deterministic term -> node -> stem -> page lookup. No model, no tokens.")
    ap.add_argument("query", nargs="*", help="free-text question or keywords")
    ap.add_argument("--facet", action="append", default=[],
                    help="one facet; repeat for each facet of the question")
    ap.add_argument("--regime", help="restrict to a regime, e.g. 'AML/CTF'")
    ap.add_argument("-k", type=int, default=config.RETRIEVE_K, help="seed nodes to keep")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)

    facets = list(args.facet)
    if args.query:
        facets.append(" ".join(args.query))
    if not facets:
        ap.error("give a query or at least one --facet")

    res = retrieve(facets, regime=args.regime, k=args.k)
    print(json.dumps(res, ensure_ascii=False, indent=2) if args.json else _render(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
