"""Arabic detection and repair.

A character class covering only U+0600-06FF scores a presentation-form document
as containing no Arabic at all - which is exactly the document most in need of
repair, and the failure mode these tests exist to prevent.
"""

import pytest

from sama import common

# "شروط فتح العضوية" as stored by a PDF that emits presentation forms in
# visual order.
PF_VISUAL = "ﺔﻳﻮﻀﻋﻟﺣ ﺍﻠﻟﺲ"
CLEAN_ARABIC = "شروط فتح العضوية لدى المؤسسة المالية"
ENGLISH = "The finance company shall verify the beneficial owner before onboarding."


class TestDetection:
    def test_presentation_forms_are_detected(self):
        assert common.pf_share(PF_VISUAL) > 0.9

    def test_clean_arabic_has_no_presentation_forms(self):
        assert common.pf_share(CLEAN_ARABIC) == 0.0

    def test_english_has_no_presentation_forms(self):
        assert common.pf_share(ENGLISH) == 0.0

    def test_arabic_share_counts_both_blocks(self):
        # A standard-block-only class would score PF_VISUAL at 0.0 here.
        assert common.arabic_share(PF_VISUAL) > 0.9
        assert common.arabic_share(CLEAN_ARABIC) > 0.9

    def test_isolated_rate_sees_presentation_forms(self):
        fragmented = "ﺔ ﻳ ﻮ ﻀ ﻋ"
        assert common.isolated_arabic_rate(fragmented) > 0.5

    def test_empty_and_whitespace_are_safe(self):
        for s in ("", "   ", "\n\n"):
            assert common.pf_share(s) == 0.0
            assert common.arabic_share(s) == 0.0
            assert common.isolated_arabic_rate(s) == 0.0


class TestRepair:
    def test_repair_removes_presentation_forms(self):
        assert common.pf_share(common.repair_arabic(PF_VISUAL)) == 0.0

    def test_repair_produces_standard_block_arabic(self):
        out = common.repair_arabic(PF_VISUAL)
        assert common.ARABIC_STD_RE.search(out)

    def test_repair_is_a_noop_on_clean_text(self):
        assert common.repair_arabic(CLEAN_ARABIC) == CLEAN_ARABIC
        assert common.repair_arabic(ENGLISH) == ENGLISH

    def test_repair_is_idempotent(self):
        once = common.repair_arabic(PF_VISUAL)
        assert common.repair_arabic(once) == once

    def test_latin_runs_keep_their_order(self):
        line = "SAMA_EN_5565 " + PF_VISUAL
        assert "SAMA_EN_5565" in common.repair_arabic(line)

    def test_multi_digit_numbers_keep_their_order(self):
        assert "2024" in common.repair_arabic(PF_VISUAL + " 2024")


class TestStripping:
    def test_strip_presentation_forms(self):
        assert common.pf_share(common.strip_presentation_forms(PF_VISUAL)) == 0.0

    def test_strip_tidies_orphaned_separators(self):
        assert common.strip_presentation_forms(f"Page 5 ({PF_VISUAL} / Introduction)") \
            == "Page 5 (Introduction)"


class TestSanitize:
    def test_lone_surrogate_is_replaced(self):
        assert common.sanitize_text("a\ud800b") == "a�b"

    def test_nulls_are_dropped(self):
        assert common.sanitize_text("a\x00b") == "ab"
