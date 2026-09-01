"""OCR routing decisions.

The presentation-form trigger is the one that is easy to omit: such a document
can carry well over a thousand characters per page and score 0.0 on a
standard-block Arabic metric, so neither the thin-text nor the isolated-Arabic
check would fire on it.
"""

import pytest

from sama import config
from sama.convert import route_for

PF_PAGE = "ﺔﻳﻮﻀﻋﻟﺣ ﺍﻠﻟﺲ " * 60
DENSE_ENGLISH = ("The finance company shall obtain and verify the identity of the "
                 "beneficial owner prior to establishing a business relationship. ") * 30


class TestRouting:
    def test_dense_english_stays_on_the_text_route(self):
        need, reason = route_for(DENSE_ENGLISH, page_count=1)
        assert need is False
        assert reason == ""

    def test_thin_text_routes_to_ocr(self):
        need, reason = route_for("a few words only", page_count=5)
        assert need is True
        assert "thin_text" in reason

    def test_presentation_forms_route_to_ocr_even_when_dense(self):
        # Dense enough to pass the thin check, and invisible to a
        # standard-block-only Arabic metric.
        need, reason = route_for(PF_PAGE, page_count=1)
        assert len(PF_PAGE) / 1 > config.THIN_CPP, "fixture must not be thin"
        assert need is True
        assert "presentation_forms" in reason

    def test_isolated_arabic_routes_to_ocr(self):
        need, reason = route_for("ب ت ث ج ح خ د ذ ر ز " * 40, page_count=1)
        assert need is True
        assert "isolated_arabic" in reason

    def test_reason_lists_every_trigger(self):
        need, reason = route_for(PF_PAGE[:100], page_count=5)
        assert need is True
        assert "thin_text" in reason and "presentation_forms" in reason

    def test_empty_document_routes_to_ocr(self):
        need, _ = route_for("", page_count=3)
        assert need is True
