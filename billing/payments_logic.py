from decimal import Decimal
from billing.overdue import is_overdue

STATUS_UNPAID = "unpaid"
STATUS_PARTIAL = "partially_paid"
STATUS_PAID = "paid"
STATUS_OVERDUE = "overdue"


def amount_due(total, amount_paid):
    """Money still to be paid (never below zero)."""
    return max(Decimal(str(total)) - Decimal(str(amount_paid)), Decimal("0.00"))


def get_status(total, amount_paid, due_date, today=None):
    """Work out the invoice status from payments and the due date."""
    total = Decimal(str(total))
    amount_paid = Decimal(str(amount_paid))

    if amount_paid >= total:
        return STATUS_PAID
    if is_overdue(due_date, amount_paid, total, today):
        return STATUS_OVERDUE
    if amount_paid > 0:
        return STATUS_PARTIAL
    return STATUS_UNPAID