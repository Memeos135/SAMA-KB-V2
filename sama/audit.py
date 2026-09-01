"""Stage 5 - read-only quality audit of the graph, vault and corpus.

Two rules govern this report:

  * A dimension that cannot be measured grades **N/A**, is excluded from the
    average, and is called out at the top.  A quality score computed over an
    empty set is not a pass - it is a missing measurement, and saying otherwise
    makes the whole report worthless.
  * Broken-Arabic exposure is measured directly from the corpus rather than from
    the conversion report, so it is available even before anything is graded.

Nothing is modified: graph.json, the vault and corpus/ are read only.
"""

from __future__ import annotations

import json
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import config
from .common import (
    md_table, pf_share, read_json, resolve_source, stem_of_source, utf8_console, write_json,
)
from .enrich import degrees, edge_key, load_enrichment, node_sources

NA = "N/A"


def grade_rank(g: Optional[str]) -> int:
    return {"A": 5, "B": 4, "C": 3, "D": 2, "F": 1}.get((g or "").upper(), 0)


def letter(x: Optional[float], a: float, b: float, c: float) -> str:
    if x is None:
        return NA
    if x >= a:
        return "A"
    if x >= b:
        return "B"
    if x >= c:
        return "C"
    return "D"


def _norm(s: str) -> str:
    s = (s or "").replace("…", " ")
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s, flags=re.UNICODE).strip().lower()


# --------------------------------------------------------------------------- #

def load_all():
    g = read_json(config.GRAPH_JSON)
    if not g:
        raise SystemExit(f"Missing {config.GRAPH_JSON}")
    nodes = g["nodes"]
    links = g.get("links") or g.get("edges") or []
    grounding = (read_json(config.GROUNDING_JSON) or {}).get("grounding") or {}
    conv_raw = read_json(config.CONV_JSON)
    conv = {d["stem"]: d for d in (conv_raw or {}).get("documents", [])}
    return nodes, links, grounding, conv, conv_raw is not None


def corpus_pf_exposure(nodes: List[dict]) -> Tuple[Dict[str, float], List[dict]]:
    """Measure broken-Arabic exposure straight from the corpus.

    Independent of the conversion report, so this number exists even on a fresh
    checkout where nothing has been graded yet.
    """
    shares: Dict[str, float] = {}
    for path in config.CORPUS_MD.glob("*.md"):
        shares[path.stem] = pf_share(path.read_text(encoding="utf-8", errors="replace"))
    bad = {s for s, v in shares.items() if v >= config.PF_SHARE_OCR}
    exposed = [n for n in nodes
               if any(stem_of_source(s) in bad for s in node_sources(n))]
    return shares, exposed


def structural(nodes, links, grounding, conv) -> dict:
    by_id = {n["id"]: n for n in nodes}
    deg = degrees(links)

    per_doc = Counter()
    for n in nodes:
        for s in node_sources(n):
            per_doc[s] += 1

    docs, npp_values = [], []
    for src, count in per_doc.items():
        stem = stem_of_source(src)
        cd = conv.get(stem, {})
        pages = cd.get("pdf_pages")
        npp = (count / pages) if pages else None
        if npp is not None and grade_rank(cd.get("grade")) >= 4:
            npp_values.append(npp)
        docs.append({"stem": stem, "nodes": count, "pdf_pages": pages,
                     "grade": cd.get("grade"), "score": cd.get("score"),
                     "nodes_per_page": round(npp, 3) if npp is not None else None,
                     "arabic_risk": cd.get("arabic_risk"), "flags": []})
    median_npp = statistics.median(npp_values) if npp_values else None

    for d in docs:
        if grade_rank(d["grade"]) == 3:
            d["flags"].append("garbled_source")
        if 0 < grade_rank(d["grade"]) <= 2:
            d["flags"].append("bad_source")
        if (median_npp and d["nodes_per_page"] is not None and grade_rank(d["grade"]) == 5
                and d["nodes_per_page"] < median_npp * config.UNDEREXTRACT_FRAC):
            d["flags"].append("under_extracted")
    docs.sort(key=lambda x: -(x["nodes"] or 0))

    dup = defaultdict(list)
    for n in nodes:
        dup[" ".join(str(n.get("norm_label") or n.get("label") or "").lower().split())].append(n)
    dup_clusters = [{"norm_label": k, "count": len(v), "labels": [m.get("label") for m in v]}
                    for k, v in dup.items() if len(v) > 1]
    dup_clusters.sort(key=lambda x: -x["count"])

    enr = load_enrichment()
    edge_keys = {edge_key(l) for l in links}
    return {
        "documents": docs,
        "median_nodes_per_page_AB": round(median_npp, 3) if median_npp is not None else None,
        "degree": {
            "isolated_count": sum(1 for n in nodes if deg[n["id"]] == 0),
            "degree1_count": sum(1 for n in nodes if deg[n["id"]] == 1),
            "top_hubs": [{"degree": d, "label": by_id[i].get("label")}
                         for i, d in sorted(deg.items(), key=lambda x: -x[1])[:10] if i in by_id],
        },
        "locators": {
            "nodes_with_source_location": sum(1 for n in nodes if n.get("source_location")
                                              or n.get("source_locations")),
            "edges_with_page_locator": sum(
                1 for k in edge_keys
                if (grounding.get(k) or {}).get("clause_a", {}) and
                (grounding.get(k) or {}).get("clause_a", {}).get("page")),
            "total_nodes": len(nodes), "total_edges": len(edge_keys),
        },
        "duplicate_clusters": dup_clusters,
        "edges": {
            "confidence": dict(Counter(l.get("confidence") for l in links)),
            "relations": dict(Counter(l.get("relation") for l in links)),
            "orphan_count": sum(1 for l in links
                                if l["source"] not in by_id or l["target"] not in by_id),
            "self_loop_count": sum(1 for l in links if l["source"] == l["target"]),
        },
        "coverage": {
            "grounded_edges": sum(1 for k in edge_keys
                                  if (grounding.get(k) or {}).get("clause_a")
                                  and (grounding.get(k) or {}).get("clause_b")),
            "edges_total": len(edge_keys),
            "node_summaries": len(enr["node"]),
            "community_blurbs": len(enr["community"]),
            "edge_narratives": len(enr["edge"]),
        },
    }


def verify_grounding(nodes, grounding) -> dict:
    """Confirm every stored excerpt really is a substring of its cited source.

    Excerpts are sliced from the corpus, so this should score 100% by
    construction.  Anything lower means a source file changed after grounding
    ran - a drift check, not a hallucination check.
    """
    by_id = {n["id"]: n for n in nodes}
    cache: Dict[str, Optional[str]] = {}

    def source_text(sf: Optional[str]) -> Optional[str]:
        if not sf:
            return None
        if sf not in cache:
            p = resolve_source(sf)
            cache[sf] = _norm(p.read_text(encoding="utf-8", errors="replace")) if p else None
        return cache[sf]

    total = checkable = ok = 0
    failures = []
    for ek, item in grounding.items():
        ids = ek.split("||")
        for side, nid in (("clause_a", ids[0]), ("clause_b", ids[1] if len(ids) > 1 else None)):
            cl = item.get(side)
            if not cl or not cl.get("excerpt"):
                continue
            total += 1
            txt = source_text(cl.get("source_file"))
            if txt is None:
                continue
            checkable += 1
            if _norm(cl["excerpt"]) in txt:
                ok += 1
            else:
                failures.append({"edge_key": ek, "side": side,
                                 "label": (by_id.get(nid) or {}).get("label"),
                                 "stem": stem_of_source(cl.get("source_file")),
                                 "excerpt": cl["excerpt"][:120]})
    return {"excerpts_total": total, "checkable": checkable, "grounded": ok,
            "rate": round(ok / checkable, 4) if checkable else None,
            "failures": failures[:100]}


def integrity() -> dict:
    try:
        out = subprocess.run([config.GRAPHIFY_BIN, "diagnose", "multigraph", "--json",
                              "--graph", str(config.GRAPH_JSON)],
                             capture_output=True, text=True, timeout=120)
        m = re.search(r"\{.*\}", (out.stdout or "").strip(), re.DOTALL)
        return {"ok": True, "data": json.loads(m.group(0))} if m else \
               {"ok": False, "raw": (out.stdout or out.stderr)[:400]}
    except Exception as e:
        return {"ok": False, "error": f"{e.__class__.__name__}: {e}"}


def score(struct, ground_res, nodes, pf_exposed, conv_present) -> dict:
    n = len(nodes) or 1

    ground_rate = ground_res["rate"]
    dims = {
        "grounding": {"grade": letter(ground_rate, config.GROUND_A, config.GROUND_B, config.GROUND_C),
                      "value": ground_rate,
                      "note": "stored excerpts still present verbatim in their source"},
        "broken_arabic_exposure": {
            "grade": letter(1 - len(pf_exposed) / n, 0.99, 0.97, 0.90),
            "value": round(len(pf_exposed) / n, 4),
            "note": "share of nodes resting on presentation-form Arabic (lower is better)"},
        "structure": {
            "grade": letter(1 - (struct["degree"]["degree1_count"]
                                 + struct["degree"]["isolated_count"]) / n, 0.75, 0.60, 0.45),
            "value": round(1 - (struct["degree"]["degree1_count"]
                                + struct["degree"]["isolated_count"]) / n, 3),
            "note": "nodes with degree >= 2"},
        "dedup": {
            "grade": letter(1 - sum(c["count"] for c in struct["duplicate_clusters"]) / n,
                            0.99, 0.95, 0.90),
            "value": round(1 - sum(c["count"] for c in struct["duplicate_clusters"]) / n, 3),
            "note": "nodes not in a duplicate-label cluster"},
        "locator_coverage": {
            "grade": letter(struct["locators"]["edges_with_page_locator"]
                            / max(struct["locators"]["total_edges"], 1), 0.90, 0.75, 0.60),
            "value": round(struct["locators"]["edges_with_page_locator"]
                           / max(struct["locators"]["total_edges"], 1), 3),
            "note": "edges carrying an exact page locator"},
    }

    # Extraction coverage depends on the conversion report.  Without it the
    # honest answer is N/A.
    if conv_present:
        a_docs = [d for d in struct["documents"] if grade_rank(d["grade"]) == 5]
        under = [d for d in a_docs if "under_extracted" in d["flags"]]
        val = 1 - (len(under) / len(a_docs)) if a_docs else None
        dims["extraction_coverage"] = {
            "grade": letter(val, 0.90, 0.75, 0.60), "value": val,
            "under_extracted": [d["stem"] for d in under],
            "note": "A-grade documents adequately covered"}
    else:
        dims["extraction_coverage"] = {
            "grade": NA, "value": None, "under_extracted": [],
            "note": "no conversion_quality.json — run the convert stage to grade this"}

    ranks = [grade_rank(d["grade"]) for d in dims.values() if d["grade"] != NA]
    avg = sum(ranks) / len(ranks) if ranks else 0
    dims["_overall"] = {"grade": {5: "A", 4: "B", 3: "C"}.get(round(avg), "D") if ranks else NA,
                        "avg_rank": round(avg, 2),
                        "dimensions_scored": len(ranks), "dimensions_na": len(dims) - len(ranks)}
    return dims


def build_report(struct, ground_res, integ, sc, nodes, links, pf_exposed, pf_shares,
                 conv_present) -> str:
    n = len(nodes)
    L = ["# Graph Quality Audit", "",
         f"> Generated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
         f"> Graph: {n} nodes, {len(links)} edges",
         "> Method: deterministic structural audit + verbatim drift check (no LLM)", ""]

    ov = sc["_overall"]
    L.append(f"## Overall grade: **{ov['grade']}**")
    if ov["dimensions_na"]:
        L.append("")
        L.append(f"> {ov['dimensions_na']} dimension(s) scored **N/A** and are excluded from the "
                 "average. An N/A is a missing measurement, not a pass.")
    L.append("")
    L.append(md_table(["Dimension", "Grade", "Value", "Note"],
                      [[k.replace("_", " ").title(), v["grade"],
                        "-" if v.get("value") is None else f"{v['value']:.1%}", v.get("note", "")]
                       for k, v in sc.items() if not k.startswith("_")]))
    L.append("")

    if not conv_present:
        L += ["> **conversion_quality.json is missing.** Extraction coverage cannot be "
              "measured and is reported as N/A. Run the convert stage to populate it.", ""]

    L += ["## Integrity (graphify diagnose multigraph)"]
    if integ.get("ok"):
        d = integ["data"]
        bad = {k: v for k, v in d.items()
               if isinstance(v, int) and v and any(w in k for w in
                                                   ("dangl", "missing", "collapse", "self_loop"))}
        L.append(f"- {'CLEAN' if not bad else 'ISSUES'} — "
                 + (", ".join(f"{k}={v}" for k, v in bad.items()) if bad else "no dangling/"
                    "missing/collapsed/self-loop edges"))
    else:
        L.append(f"- unavailable: {integ.get('error') or integ.get('raw', '')}")
    L.append("")

    L += ["## Broken-Arabic exposure (measured from the corpus)", "",
          f"- Corpus documents with presentation-form Arabic >= {config.PF_SHARE_OCR:.0%}: "
          f"**{sum(1 for v in pf_shares.values() if v >= config.PF_SHARE_OCR)}** "
          f"of {len(pf_shares)}",
          f"- Nodes resting on those documents: **{len(pf_exposed)} / {n}** "
          f"({len(pf_exposed) / max(n, 1):.1%})", ""]
    worst = sorted(pf_shares.items(), key=lambda x: -x[1])[:12]
    if worst and worst[0][1] > 0:
        L += [md_table(["Stem", "Presentation-form share"],
                       [[f"`{s}`", f"{v:.1%}"] for s, v in worst if v > 0]), ""]

    L += ["## Grounding drift", "",
          f"- Stored excerpts: **{ground_res['excerpts_total']}** "
          f"(checkable: {ground_res['checkable']})",
          f"- Still verbatim in source: **{ground_res['grounded']}** → "
          f"**{ground_res['rate']:.1%}**" if ground_res["rate"] is not None
          else "- rate: n/a", "",
          "_Excerpts are sliced directly from the corpus, so this should read 100%. "
          "Anything lower means a source file changed after grounding ran — re-run the "
          "ground stage._", ""]
    if ground_res["failures"]:
        L += ["<details><summary>Drifted excerpts</summary>", "",
              md_table(["Node", "Stem", "Excerpt"],
                       [[f["label"], f["stem"], f["excerpt"][:80]]
                        for f in ground_res["failures"]]), "", "</details>", ""]

    lc = struct["locators"]
    L += ["## Locators", "",
          f"- Edges with an exact page locator: **{lc['edges_with_page_locator']} / "
          f"{lc['total_edges']}**",
          f"- Nodes carrying source_location from extraction: "
          f"**{lc['nodes_with_source_location']} / {lc['total_nodes']}**", ""]

    cov = struct["coverage"]
    L += ["## Enrichment coverage", "",
          f"- Node summaries: **{cov['node_summaries']} / {len(nodes)}**",
          f"- Community blurbs: **{cov['community_blurbs']}**",
          f"- Edge narratives: **{cov['edge_narratives']}** "
          f"(selective by design — grounding covers every edge)", ""]

    dg = struct["degree"]
    L += ["## Structure", "",
          f"- Isolated: **{dg['isolated_count']}** · degree-1: **{dg['degree1_count']}** "
          f"({dg['degree1_count'] / max(n, 1):.0%})",
          "- Top hubs: " + ", ".join(f"{h['label']} ({h['degree']})" for h in dg["top_hubs"][:6]),
          ""]

    ed = struct["edges"]
    L += ["## Edges", "",
          "- Confidence: " + ", ".join(f"{k}={v}" for k, v in ed["confidence"].items()),
          "- Relations: " + ", ".join(f"{k}={v}" for k, v in
                                      sorted(ed["relations"].items(), key=lambda x: -x[1])[:10]),
          f"- Orphans: {ed['orphan_count']} · self-loops: {ed['self_loop_count']}", ""]

    L += ["## Duplicate-label clusters", ""]
    if struct["duplicate_clusters"]:
        L.append(md_table(["norm_label", "count", "labels"],
                          [[c["norm_label"], c["count"], "; ".join(str(x) for x in c["labels"][:6])]
                           for c in struct["duplicate_clusters"][:40]]))
    else:
        L.append("- none (dedup ran)")
    L.append("")

    L += ["## Per-document coverage", ""]
    if conv_present:
        L.append(md_table(["Stem", "Nodes", "Pages", "Nodes/pg", "Grade", "Flags"],
                          [[d["stem"], d["nodes"], d["pdf_pages"], d["nodes_per_page"],
                            d["grade"] or NA, ", ".join(d["flags"]) or "-"]
                           for d in struct["documents"][:200]]))
    else:
        L.append("_Requires conversion_quality.json._")
    L.append("")

    fixes = []
    if pf_exposed:
        fixes.append(f"**Re-convert the {sum(1 for v in pf_shares.values() if v >= config.PF_SHARE_OCR)} "
                     f"presentation-form documents** — {len(pf_exposed)} nodes "
                     f"({len(pf_exposed) / max(n, 1):.0%}) rest on unreadable Arabic.")
    if not conv_present:
        fixes.append("**Run the convert stage** so extraction coverage stops reading N/A.")
    if struct["duplicate_clusters"]:
        fixes.append(f"**{len(struct['duplicate_clusters'])} duplicate-label clusters remain** — "
                     "re-run the build stage with dedup enabled.")
    if ground_res["rate"] is not None and ground_res["rate"] < 0.999:
        fixes.append("**Grounding has drifted from the corpus** — re-run the ground stage.")
    if dg["degree1_count"] / max(n, 1) > 0.30:
        fixes.append(f"**{dg['degree1_count']} degree-1 nodes** — consider a deeper extraction pass.")
    L += ["## Prioritized fixes", ""]
    L += [f"{i}. {f}" for i, f in enumerate(fixes, 1)] or ["- No high-priority issues detected."]
    L.append("")
    return "\n".join(L)


def run() -> int:
    utf8_console()
    nodes, links, grounding, conv, conv_present = load_all()
    print(f"Loaded {len(nodes)} nodes, {len(links)} edges, {len(grounding)} grounded edges, "
          f"{len(conv)} conversion records")

    pf_shares, pf_exposed = corpus_pf_exposure(nodes)
    struct = structural(nodes, links, grounding, conv)
    ground_res = verify_grounding(nodes, grounding)
    integ = integrity()
    sc = score(struct, ground_res, nodes, pf_exposed, conv_present)

    config.GRAPH_REPORTS.mkdir(parents=True, exist_ok=True)
    write_json(config.GRAPH_REPORTS / "graph_quality_audit.json", {
        "generated": datetime.now(timezone.utc).isoformat(),
        "conversion_report_present": conv_present,
        "scores": sc, "structural": struct,
        "grounding": {k: v for k, v in ground_res.items() if k != "failures"},
        "grounding_failures": ground_res["failures"],
        "broken_arabic": {"exposed_nodes": len(pf_exposed),
                          "documents": {k: round(v, 4) for k, v in pf_shares.items() if v > 0}},
        "integrity": integ,
    })
    report = config.GRAPH_REPORTS / "GRAPH_QUALITY_AUDIT.md"
    report.write_text(build_report(struct, ground_res, integ, sc, nodes, links,
                                   pf_exposed, pf_shares, conv_present), encoding="utf-8")

    print(f"Overall grade: {sc['_overall']['grade']} "
          f"({sc['_overall']['dimensions_na']} dimension(s) N/A)")
    print(f"Wrote {report}")
    return 0
