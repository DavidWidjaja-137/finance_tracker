from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpRequest
from django.views import View

from finance.models import TransactionType, Transaction, TransactionCategory, Account


class TransactionView(View):

    def get(self, request: HttpRequest):

        filter_start = (
            datetime.strptime(request.GET["filter_start"], "%Y-%m").date() if "filter_start" in request.GET else None
        )
        filter_end = (
            datetime.strptime(request.GET["filter_end"], "%Y-%m").date() if "filter_end" in request.GET else None
        )
        transaction_type = (
            request.GET["transaction_type_selector"]
            if "transaction_type_selector" in request.GET and request.GET["transaction_type_selector"] != ""
            else None
        )
        transaction_category = (
            request.GET["transaction_category_selector"]
            if "transaction_category_selector" in request.GET and request.GET["transaction_category_selector"] != ""
            else None
        )

        account = (
            str(request.GET["transaction_account_selector"])
            if "transaction_account_selector" in request.GET and request.GET["transaction_account_selector"] != "All"
            else None
        )

        transaction_filter = Transaction.objects
        if account:
            transaction_filter = transaction_filter.filter(account__name=account)

        if transaction_type and filter_start and filter_end:
            transactions = (
                transaction_filter.filter(mapping__type__name=transaction_type)
                .filter(date__range=(filter_start, filter_end))
                .all()
            )
        elif transaction_category and filter_start and filter_end:
            transactions = (
                transaction_filter.filter(mapping__type__category__name=transaction_category)
                .filter(date__range=(filter_start, filter_end))
                .all()
            )
        else:
            transactions = []

        context = {
            "transaction_accounts": Account.objects.all(),
            "transactions": transactions,
            "transaction_type": TransactionType.objects.all(),
            "transaction_category": TransactionCategory.objects.all(),
        }

        return render(request, "finance/transactions.html", context)
