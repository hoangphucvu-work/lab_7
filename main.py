from business_rules import (
    calculate_total,
    requires_review,
    get_approval_tier,
    apply_discount,
)

# add sample inputs
price, qty = 450.00, 3
total = calculate_total(price, qty)

print(f"Total: $f{total:.2f}")
print(f"Requires approval: {requires_review(total)}")
print(f"Approval tier: {get_approval_tier(total)}")
print(f"10% discount applied: ${apply_discount(total, 10):.2f}")
