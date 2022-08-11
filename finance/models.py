from django.contrib.auth.models import User
from django.db import models
from user.shared.SoftDeleteModel import SoftDeleteModel


class Income(SoftDeleteModel):
    sector = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)


class Budget(SoftDeleteModel):
    sector = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    percent = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)


class Expense(SoftDeleteModel):
    sector = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True)
