from django.db import models

# create database models(like an ORM) here


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class TransactionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):

        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT)

    def __str__(self):

        return self.name


class TransactionMap(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)

    class Meta:
        unique_together = ["name", "type"]

    def __str__(self):

        return self.name


class TransactionFlow(models.TextChoices):
    INFLOW = "INFLOW"
    OUTFLOW = "OUTFLOW"


class Transaction(models.Model):
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    mapping = models.ForeignKey(TransactionMap, on_delete=models.PROTECT)
    amount = models.FloatField()
    flow = models.CharField(max_length=10, choices=TransactionFlow)
