from django.db import models


class Product(models.Model):
    PRODUCT_TYPES = [
        ('software', 'Software'),
        ('service', 'Service'),
        ('subscription', 'Subscription'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPES,
        default='software'
    )

    sales_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    variant_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    sales_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.variant_name}"