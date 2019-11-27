from django.db import models
from djmoney.models.fields import MoneyField


class ExampleModelWithMoneyFieldFromTheGetGo(models.Model):
    """
    This model has the display field from the get go
    """
    display = MoneyField(max_digits=20, decimal_places=4, null=True, default_currency=None)


class ExampleModelWithLaterAddedMoneyField(models.Model):
    """
    This model has the display field from the get go
    """
    dummy_field = models.CharField(max_length=10)
    display = MoneyField(max_digits=20, decimal_places=4, null=True, default_currency=None)

    another_nullable_field_but_without_default = MoneyField(max_digits=20, decimal_places=4, null=True)
