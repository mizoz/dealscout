from deal_scout.filters import passes_filters
from deal_scout.models import Deal


def test_blocks_listed_terms():
    deal = Deal(title="Refurbished blender $39.99", source="test", url="https://example.com")
    assert not passes_filters(deal, blocked_keywords=["refurbished", "subscription"])


def test_allows_matching_deal():
    deal = Deal(title="Cologne tester $15.15", source="test", url="https://example.com")
    assert passes_filters(deal, blocked_keywords=["refurbished", "subscription"], include_keywords=["cologne"])

