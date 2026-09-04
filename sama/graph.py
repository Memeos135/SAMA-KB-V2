"""Stage 3 - build the knowledge graph, deduplicate it, export the vault.

The live graph is snapshotted before anything runs and replaced only once a new
extraction has succeeded, so a failed build cannot leave it half-updated.

Order matters: dedup runs between extract and cluster, so the community pass and
the Obsidian export both see one node per entity rather than one per
(entity, source document).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from . import config
from .common import read_json, write_json


def _run(args: List[str], step: str) -> None:
    print(f"\n=== {step} ===\n$ {' '.join(args)}", flush=True)
    proc = subprocess.run(args, cwd=str(config.ROOT))
    if proc.returncode != 0:
        raise RuntimeError(f"{step} failed (exit {proc.returncode})")


def check_prereqs() -> None:
    if shutil.which(config.GRAPHIFY_BIN) is None:
        raise SystemExit(
            f"'{config.GRAPHIFY_BIN}' is not on PATH.\n"
            "  Install it, or point SAMA config at it:  export GRAPHIFY_BIN=/path/to/graphify"
        )
    if not os.environ.get(config.GRAPHIFY_API_KEY_ENV, "").strip():
        raise SystemExit(
            f"{config.GRAPHIFY_API_KEY_ENV} is not set (graphify needs it for extraction).\n"
            f'  export {config.GRAPHIFY_API_KEY_ENV}="sk-ant-..."'
        )


def snapshot() -> Optional[Path]:
    """Copy the live graph aside before touching it."""
    if not config.GRAPH_JSON.exists():
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = config.SNAPSHOTS / f"graphify-out_{stamp}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(config.GRAPH_DIR, dest)
    print(f"Snapshot: {dest}")
    return dest


def extract(force: bool = True) -> None:
    """Extract into corpus/graphify-out, then promote only on success."""
    staged = config.CORPUS_DIR / "graphify-out"
    if staged.exists():
        shutil.rmtree(staged)

    # Converted .md is gitignored (re-derivable). Graphify honors .gitignore,
    # so without this flag extract sees an empty corpus.
    args = [config.GRAPHIFY_BIN, "extract", str(config.CORPUS_DIR.name),
            "--no-gitignore",
            "--mode", config.GRAPHIFY_MODE, "--backend", "claude",
            "--model", config.GRAPHIFY_MODEL]
    if force:
        args.insert(3, "--force")
    _run(args, "graphify extract")

    if not (staged / "graph.json").exists():
        raise RuntimeError(f"extract produced no graph at {staged} — live graph left untouched")

    # Promote: the previous graph is only replaced once a good one exists.
    if config.GRAPH_DIR.exists():
        shutil.rmtree(config.GRAPH_DIR)
    shutil.move(str(staged), str(config.GRAPH_DIR))
    print(f"Promoted new graph -> {config.GRAPH_DIR}")


# --------------------------------------------------------------------------- #
# Node dedup
# --------------------------------------------------------------------------- #

def _norm_key(node: dict) -> str:
    raw = (node.get("norm_label") or node.get("label") or node["id"])
    return " ".join(str(raw).lower().split())


def dedup(graph_path: Optional[Path] = None) -> dict:
    """Merge nodes that denote the same entity extracted from different PDFs.

    Extraction emits one node per (entity, source document), so a law cited by
    ten circulars becomes ten near-identical notes and a reader cannot tell which
    is authoritative.  Merging on normalised label keeps a single canonical node
    carrying every source.
    """
    is_live = graph_path is None or graph_path == config.GRAPH_JSON
    graph_path = graph_path or config.GRAPH_JSON
    g = read_json(graph_path)
    if not g:
        raise SystemExit(f"Missing {graph_path}")
    nodes: List[dict] = g["nodes"]
    links: List[dict] = g.get("links") or g.get("edges") or []

    groups: Dict[str, List[dict]] = defaultdict(list)
    for n in nodes:
        groups[_norm_key(n)].append(n)

    degree: Dict[str, int] = defaultdict(int)
    for l in links:
        degree[l["source"]] += 1
        degree[l["target"]] += 1

    remap: Dict[str, str] = {}
    merged: List[dict] = []
    clusters_merged = 0
    for key, members in groups.items():
        if len(members) == 1:
            merged.append(members[0])
            remap[members[0]["id"]] = members[0]["id"]
            continue
        clusters_merged += 1
        # Canonical = best connected, tie-broken by the label without a _N suffix.
        canon = sorted(
            members,
            key=lambda n: (-degree[n["id"]], len(str(n.get("label") or "")), str(n["id"])),
        )[0]
        sources, urls, locations = [], [], []
        for m in members:
            remap[m["id"]] = canon["id"]
            for field, bucket in (("source_file", sources), ("source_url", urls),
                                  ("source_location", locations)):
                v = m.get(field)
                if v and v not in bucket:
                    bucket.append(v)
        node = dict(canon)
        node["source_files"] = sources
        node["source_urls"] = urls
        node["source_locations"] = [x for x in locations if x]
        node["merged_from"] = [m["id"] for m in members if m["id"] != canon["id"]]
        merged.append(node)

    # Rewrite edges onto canonical ids, dropping self-loops and parallel edges.
    seen: Dict[Tuple[str, str, str], dict] = {}
    conf_rank = {"EXTRACTED": 3, "INFERRED": 2, "AMBIGUOUS": 1}
    dropped_self = 0
    for l in links:
        s, t = remap.get(l["source"], l["source"]), remap.get(l["target"], l["target"])
        if s == t:
            dropped_self += 1
            continue
        a, b = sorted([s, t])
        key = (a, b, l.get("relation", ""))
        new = dict(l, source=s, target=t)
        cur = seen.get(key)
        if cur is None or conf_rank.get(new.get("confidence"), 0) > conf_rank.get(cur.get("confidence"), 0):
            seen[key] = new
    new_links = list(seen.values())

    g["nodes"] = merged
    if "links" in g:
        g["links"] = new_links
    else:
        g["edges"] = new_links

    stats = {
        "nodes_before": len(nodes), "nodes_after": len(merged),
        "edges_before": len(links), "edges_after": len(new_links),
        "clusters_merged": clusters_merged,
        "self_loops_dropped": dropped_self,
        "parallel_edges_dropped": len(links) - dropped_self - len(new_links),
    }
    write_json(graph_path, g)
    if is_live:   # only report on the project's own graph, never a caller's copy
        write_json(config.GRAPH_REPORTS / "dedup.json",
                   {"generated": datetime.now(timezone.utc).isoformat(), **stats})
    print(f"Dedup: {stats['nodes_before']} -> {stats['nodes_after']} nodes "
          f"({clusters_merged} clusters merged), "
          f"{stats['edges_before']} -> {stats['edges_after']} edges")
    return stats


# --------------------------------------------------------------------------- #
# Cluster / label / export
# --------------------------------------------------------------------------- #

def cluster_and_label() -> None:
    common = ["--backend", "claude", "--model", config.GRAPHIFY_MODEL]
    _run([config.GRAPHIFY_BIN, "cluster-only", "."] + common, "graphify cluster-only")
    _run([config.GRAPHIFY_BIN, "label", "."] + common, "graphify label")


def export_vault() -> None:
    config.VAULT_DIR.mkdir(parents=True, exist_ok=True)
    _run([config.GRAPHIFY_BIN, "export", "obsidian", "--dir", str(config.VAULT_DIR)],
         "graphify export obsidian")


def fix_wikilinks(dry_run: bool = False) -> int:
    """Repair links written with characters the exported filenames strip.

    An export drops filesystem-forbidden characters from note filenames, but the
    links inside notes keep the original label, so `[[AML/CTF Guide]]` fails to
    resolve and - for '/' - renders as a phantom node.  Rewriting to the alias
    form fixes the target while keeping the readable display text.
    """
    from .common import strip_forbidden

    import re
    link_re = re.compile(r"\[\[([^\]\|]+)(\|[^\]]+)?\]\]")
    existing = {p.stem for p in config.VAULT_DIR.glob("*.md")}
    total = files = 0

    for md in config.VAULT_DIR.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        changed = 0

        def repl(m):
            nonlocal changed
            target, alias = m.group(1).strip(), m.group(2)
            if target in existing:
                return m.group(0)
            stripped = strip_forbidden(target)
            if stripped != target and stripped in existing:
                changed += 1
                return f"[[{stripped}{alias}]]" if alias else f"[[{stripped}|{target}]]"
            return m.group(0)

        new = link_re.sub(repl, text)
        if changed:
            total += changed
            files += 1
            if not dry_run:
                md.write_text(new, encoding="utf-8")

    print(f"{'Would rewrite' if dry_run else 'Rewrote'} {total} wikilink(s) across {files} file(s)")
    return total


def run(skip_extract: bool = False, no_dedup: bool = False, force: bool = True) -> int:
    config.ensure_dirs()
    if not list(config.CORPUS_MD.glob("*.md")):
        print("corpus/markdown is empty — run the convert stage first.")
        return 1

    check_prereqs()
    snapshot()
    if not skip_extract:
        extract(force=force)
    if config.DEDUP_NODES and not no_dedup:
        dedup()
    cluster_and_label()
    export_vault()
    fix_wikilinks()

    g = read_json(config.GRAPH_JSON, {})
    print(f"\nGraph: {len(g.get('nodes', []))} nodes, "
          f"{len(g.get('links') or g.get('edges') or [])} edges")
    print(f"Vault: {len(list(config.VAULT_DIR.glob('*.md')))} notes -> {config.VAULT_DIR}")
    return 0
