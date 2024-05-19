from datetime import date, datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.forms import ModelForm, SelectDateWidget, Form

from finance.models import (
    Account,
    TransactionType,
    TransactionCategory,
    TransactionMap,
    Transaction
)
from finance.importer.importer import import_transactions

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["name", "description"]


class TransactionTypeForm(ModelForm):
    class Meta:
        model = TransactionType
        fields = ["name", "description", "category"]


class TransactionCategoryForm(ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ["name", "description"]


class TransactionMapForm(ModelForm):
    class Meta:
        model = TransactionMap
        fields = ["name", "description", "type"]


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "account", "mapping", "amount", "flow"]
        widgets = {
            "date": SelectDateWidget(),
        }

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the finance index.")


def account(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = AccountForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/account")

    else:   
        all_accounts = Account.objects.all()
        context = {
            "all_accounts": all_accounts,
            "form": AccountForm()
        }

        return render(request, "finance/accounts.html", context)


def transaction_type(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = TransactionTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/transaction_type")
        
    else:
        transaction_types = TransactionType.objects.all()
        context = {
            "transaction_types": transaction_types,
            "form": TransactionTypeForm()
        }

        return render(request, "finance/transaction_types.html", context)


def transaction_category(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = TransactionCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/transaction_category")
        
    else:
        transaction_categories = TransactionCategory.objects.all()
        context = {
            "transaction_categories": transaction_categories,
            "form": TransactionCategoryForm()
        }

        return render(request, "finance/transaction_categories.html", context)


def transaction_map(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = TransactionMapForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/transaction_map")
        
    else:
        transaction_maps = TransactionMap.objects.all()
        context = {
            "transaction_maps": transaction_maps,
            "form": TransactionMapForm()
        }

        return render(request, "finance/transaction_maps.html", context)


def transaction(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        start = datetime.strptime(request.POST["start"], '%Y-%m').date()
        end = datetime.strptime(request.POST["end"], '%Y-%m').date()

        import_transactions(start, end)

        return HttpResponseRedirect("/finance/transaction")
        
    else:
        accounts = Account.objects.all()
        transactions = Transaction.objects.all()
        context = {
            "transactions": transactions,
            "accounts": accounts

        }

        return render(request, "finance/transactions.html", context)
