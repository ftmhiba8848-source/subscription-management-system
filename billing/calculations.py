from decimal import Decimal, ROUND_HALF_UP


def money(value):
    """Round to 2 decimal places, like real money."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_totals(subtotal, discount_percent=0, tax_percent=0):
    """
    Rule used for now: discount first, then tax on the reduced amount.
    (This is one of our open questions, so we may change it later.)
    """
    subtotal = Decimal(str(subtotal))
    discount = subtotal * Decimal(str(discount_percent)) / 100
    taxable = subtotal - discount
    tax = taxable * Decimal(str(tax_percent)) / 100
    total = taxable + tax

    return {
        "subtotal": money(subtotal),
        "discount": money(discount),
        "taxable": money(taxable),
        "tax": money(tax),
        "total": money(total),
    }