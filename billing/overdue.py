from datetime import date, timedelta

# Open question: confirm the real rule with the team.
# For now we assume invoices are due 15 days after the invoice date.
DEFAULT_DUE_DAYS = 15


def get_due_date(invoice_date, due_days=DEFAULT_DUE_DAYS):
    """Due date = invoice date + number of days."""
    return invoice_date + timedelta(days=due_days)


def is_overdue(due_date, amount_paid, total, today=None):
    """An invoice is overdue if it is past the due date and not fully paid."""
    if today is None:
        today = date.today()
    return today > due_date and amount_paid < total


def days_overdue(due_date, today=None):
    """How many days late (0 if not late)."""
    if today is None:
        today = date.today()
    return max((today - due_date).days, 0)
