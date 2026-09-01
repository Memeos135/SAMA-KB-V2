"""Page maps, wikilinks, deterministic grounding and node dedup."""

import json

import pytest

from sama import common
from sama.graph import dedup

SAMPLE_MD = """# SAMA_EN_1234_VER1.pdf

## Page 1

The Anti-Money Laundering Law defines a customer as any natural or legal person
who enters into a business relationship with a financial institution.

## Page 2

Customer due diligence measures shall be applied by the finance company before
establishing any business relationship with a merchant.
"""


class TestPageMap:
    def test_pages_are_split(self):
        pages = common.parse_md_pages(SAMPLE_MD)
        assert [p.number for p in pages] == [1, 2]

    def test_offsets_locate_the_right_page(self):
        pages = common.parse_md_pages(SAMPLE_MD)
        off = SAMPLE_MD.index("merchant")
        assert common.page_for_offset(pages, off) == 2

    def test_document_without_page_headers_becomes_one_page(self):
        pages = common.parse_md_pages("# Title\n\nSome body text here.")
        assert len(pages) == 1 and pages[0].number == 1

    def test_roundtrip_through_pages_to_md(self):
        md = common.pages_to_md("doc.pdf", ["first page", "second page"])
        assert [p.number for p in common.parse_md_pages(md)] == [1, 2]


class TestWikilinks:
    def test_plain_label_is_untouched(self):
        assert common.wikilink("Banking Control Law") == "[[Banking Control Law]]"

    def test_slash_label_uses_the_alias_form(self):
        # A raw [[AML/CTF Guide]] would not resolve and would spawn a phantom node.
        assert common.wikilink("AML/CTF Guide") == "[[AMLCTF Guide|AML/CTF Guide]]"

    def test_colon_label_uses_the_alias_form(self):
        assert common.wikilink("Circular: 123") == "[[Circular 123|Circular: 123]]"

    def test_strip_forbidden_matches_export_naming(self):
        assert common.strip_forbidden('a<b>c:d"e/f\\g|h?i*j') == "abcdefghij"


class TestStems:
    @pytest.mark.parametrize("name,expected", [
        ("SAMA_EN_1234_VER1.pdf", "SAMA_EN_1234_VER1"),
        ("SAMA_EN_10593_VER1_0.md", "SAMA_EN_10593_VER1_0"),
        ("sama_en_853_ver1.pdf", "SAMA_EN_853_VER1"),
    ])
    def test_sama_stems_are_normalised(self, name, expected):
        assert common.stem_for(name) == expected

    def test_arabic_filename_keeps_its_name(self):
        assert common.stem_for("النموذج السنوي.pdf") == "النموذج السنوي"


class TestGrounding:
    def test_excerpt_is_a_literal_slice_of_the_source(self, tmp_path, monkeypatch):
        from sama import config, enrich

        md = tmp_path / "markdown"
        md.mkdir()
        (md / "SAMA_EN_1234_VER1.md").write_text(SAMPLE_MD, encoding="utf-8")
        monkeypatch.setattr(config, "CORPUS_DIR", tmp_path)
        monkeypatch.setattr(config, "CORPUS_MD", md)
        enrich._source_cache.clear()

        node = {"id": "n1", "label": "Customer Due Diligence",
                "source_file": "markdown/SAMA_EN_1234_VER1.md"}
        got = enrich.best_excerpt(node, "Finance Company")

        assert got is not None
        # verbatim by construction: normalised excerpt must appear in the source
        assert " ".join(got["excerpt"].split()) in " ".join(SAMPLE_MD.split())
        assert got["page"] == 2          # exact locator, not a model guess

    def test_missing_source_yields_no_excerpt(self, tmp_path, monkeypatch):
        from sama import config, enrich

        monkeypatch.setattr(config, "CORPUS_DIR", tmp_path)
        monkeypatch.setattr(config, "CORPUS_MD", tmp_path)
        enrich._source_cache.clear()
        assert enrich.best_excerpt(
            {"id": "n", "label": "Whatever", "source_file": "nope.md"}, "Other") is None


class TestDedup:
    def _graph(self):
        return {
            "nodes": [
                {"id": "a1", "label": "Banking Control Law", "norm_label": "banking control law",
                 "source_file": "markdown/SAMA_EN_1.md"},
                {"id": "a2", "label": "Banking Control Law_1", "norm_label": "banking control law",
                 "source_file": "markdown/SAMA_EN_2.md"},
                {"id": "b1", "label": "Finance Company", "norm_label": "finance company",
                 "source_file": "markdown/SAMA_EN_3.md"},
            ],
            "links": [
                {"source": "a1", "target": "b1", "relation": "defines", "confidence": "EXTRACTED"},
                {"source": "a2", "target": "b1", "relation": "defines", "confidence": "INFERRED"},
            ],
        }

    def test_duplicate_labels_collapse(self, tmp_path):
        p = tmp_path / "graph.json"
        p.write_text(json.dumps(self._graph()), encoding="utf-8")
        stats = dedup(p)
        assert stats["nodes_before"] == 3 and stats["nodes_after"] == 2
        assert stats["clusters_merged"] == 1

    def test_every_source_is_preserved(self, tmp_path):
        p = tmp_path / "graph.json"
        p.write_text(json.dumps(self._graph()), encoding="utf-8")
        dedup(p)
        merged = json.loads(p.read_text(encoding="utf-8"))
        law = [n for n in merged["nodes"] if "banking" in n["norm_label"]][0]
        assert sorted(law["source_files"]) == ["markdown/SAMA_EN_1.md", "markdown/SAMA_EN_2.md"]

    def test_parallel_edges_collapse_keeping_best_confidence(self, tmp_path):
        p = tmp_path / "graph.json"
        p.write_text(json.dumps(self._graph()), encoding="utf-8")
        dedup(p)
        merged = json.loads(p.read_text(encoding="utf-8"))
        assert len(merged["links"]) == 1
        assert merged["links"][0]["confidence"] == "EXTRACTED"

    def test_self_loops_created_by_merging_are_dropped(self, tmp_path):
        g = self._graph()
        g["links"].append({"source": "a1", "target": "a2", "relation": "same_as",
                           "confidence": "INFERRED"})
        p = tmp_path / "graph.json"
        p.write_text(json.dumps(g), encoding="utf-8")
        stats = dedup(p)
        assert stats["self_loops_dropped"] == 1


class TestAuditHonesty:
    def test_missing_measurement_grades_na_not_a(self):
        """A dimension computed over no data must not score as a pass."""
        from sama.audit import NA, letter
        assert letter(None, 0.9, 0.75, 0.6) == NA
        assert letter(0.95, 0.9, 0.75, 0.6) == "A"
