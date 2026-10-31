from django.contrib import admin

from .models import Discount, Invoice, InvoiceLine, Payment, Tax


class InvoiceLineInline(admin.TabularInline):
    model = InvoiceLine
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "subscription", "status", "due_date", "total")
    list_filter = ("status",)
    inlines = [InvoiceLineInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice", "amount", "method", "paid_on")
    list_filter = ("method",)


admin.site.register(Tax)
admin.site.register(Discount)
