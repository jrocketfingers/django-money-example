from djmoney.contrib.django_rest_framework.fields import MoneyField
from rest_framework import serializers

from core import models


class ExampleSerializer(serializers.ModelSerializer):
    display_amount = MoneyField(source="display", currency_field_name="display_currency")

    class Meta:
        model = models.ExampleModelWithMoneyFieldFromTheGetGo
        fields = ("display_amount", "display_currency",)
