from django.db import models


class Subscription(models.Model):
    customer_name = models.CharField(max_length=200)
    plan_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default="active")

    def __str__(self):
        return f"{self.customer_name} - {self.plan_name}"
    