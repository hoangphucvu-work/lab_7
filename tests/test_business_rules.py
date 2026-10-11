from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)


def tests_requires_review_over():
    assert requires_review(1500) is True


def tests_requires_review_under():
    assert requires_review(690) is False


def tests_requires_at_limit():
    # Exactly at 1000 should not require review
    assert requires_review(1000) is False


def tests_total_with_tax():
    assert round(calculate_total(100, 2), 2) == 214.00


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():
    assert get_approval_tier(500) == "auto"  # exactly at limit


def test_tier_manager():
    assert get_approval_tier(1500) == "manager"


def test_discount_ten():
    assert apply_discount(100.00, 10) == 90.0
