from datetime import date
from decimal import Decimal

from django.db.models import DecimalField, F, Sum, Value
from django.db.models.functions import Coalesce
from django.shortcuts import render

from .models import Invoice, Payment

ZERO = Value(Decimal("0.00"), output_field=DecimalField(max_digits=12, decimal_places=2))


def dashboard(request):
    today = date.today()

    sent = Invoice.objects.exclude(status=Invoice.DRAFT)

    total_invoiced = sent.aggregate(t=Coalesce(Sum("total"), ZERO))["t"]
    total_collected = Payment.objects.aggregate(t=Coalesce(Sum("amount"), ZERO))["t"]

    unpaid = sent.annotate(paid=Coalesce(Sum("payments__amount"), ZERO)).filter(
        paid__lt=F("total")
    )
    overdue = unpaid.filter(due_date__lt=today)

    outstanding = unpaid.aggregate(t=Coalesce(Sum(F("total") - F("paid")), ZERO))["t"]
    overdue_amount = overdue.aggregate(t=Coalesce(Sum(F("total") - F("paid")), ZERO))["t"]

    context = {
        "total_invoiced": total_invoiced,
        "total_collected": total_collected,
        "outstanding": outstanding,
        "overdue_amount": overdue_amount,
        "overdue_count": overdue.count(),
        "invoice_count": sent.count(),
        "recent_payments": Payment.objects.select_related("invoice").order_by("-paid_on")[:5],
    }
    return render(request, "billing/dashboard.html", context)