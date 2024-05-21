from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.forms import ModelForm, SelectDateWidget

from finance.models import Account, TransactionType, TransactionCategory, TransactionMap, Transaction
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
        context = {"all_accounts": all_accounts, "form": AccountForm()}

        return render(request, "finance/accounts.html", context)


def transaction_type(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = TransactionTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/transaction_type")

    else:
        transaction_types = TransactionType.objects.all()
        context = {"transaction_types": transaction_types, "form": TransactionTypeForm()}

        return render(request, "finance/transaction_types.html", context)


def transaction_category(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        form = TransactionCategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/finance/transaction_category")
        else:
            raise ValueError("Form is invalid.")

    else:
        transaction_categories = TransactionCategory.objects.all()
        context = {"transaction_categories": transaction_categories, "form": TransactionCategoryForm()}

        return render(request, "finance/transaction_categories.html", context)


def update_transaction_map(request: HttpRequest) -> HttpResponse:
    """
    Updates the description and type of a transaction map.
    """

    if request.method == "POST":

        transaction_type = (
            str(request.POST["type"]) if "type" in request.POST and request.POST["type"] not in ["", "None"] else None
        )
        transaction_map_id = (
            str(request.POST["id"]) if "id" in request.POST and request.POST["id"] not in ["", "None"] else None
        )
        transaction_description = (
            str(request.POST["description"])
            if "description" in request.POST and request.POST["description"] not in ["", "None"]
            else None
        )

        if transaction_type and transaction_map_id and transaction_description:
            map = TransactionMap.objects.get(id=transaction_map_id)
            map.description = transaction_description
            map.type = TransactionType.objects.get(id=transaction_type)
            map.save()

        return HttpResponseRedirect("/finance/transaction_map")

    else:

        raise ValueError("Invalid Request Method.")


def insert_transaction_map(request: HttpRequest) -> HttpResponse:
    """
    Inserts a new transaction map
    """

    if request.method == "POST":

        transaction_type = (
            str(request.POST["type"]) if "type" in request.POST and request.POST["type"] not in ["", "None"] else None
        )
        transaction_map_name = (
            str(request.POST["name"]) if "name" in request.POST and request.POST["name"] not in ["", "None"] else None
        )
        transaction_description = (
            str(request.POST["description"])
            if "description" in request.POST and request.POST["description"] not in ["", "None"]
            else None
        )

        if transaction_type and transaction_map_name and transaction_description:
            TransactionMap.objects.create(
                name=transaction_map_name,
                description=transaction_description,
                type=TransactionType.objects.get(id=transaction_type),
            )

        return HttpResponseRedirect("/finance/transaction_map")

    else:

        raise ValueError("Invalid Request Method.")


def transaction_map(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":

        transaction_type = (
            str(request.GET["transaction_type_selector"])
            if "transaction_type_selector" in request.GET
            and request.GET["transaction_type_selector"] not in ["", "None"]
            else None
        )
        transaction_category = (
            str(request.GET["transaction_category_selector"])
            if "transaction_category_selector" in request.GET
            and request.GET["transaction_category_selector"] not in ["", "None"]
            else None
        )

        if transaction_type:
            transaction_maps = TransactionMap.objects.filter(type__name=transaction_type).all()
        elif transaction_category:
            transaction_maps = TransactionMap.objects.filter(type__category__name=transaction_category).all()
        else:
            transaction_maps = []

        # check if a transaction map is included.
        transaction_map_id = (
            str(request.GET["transaction_map_selector"])
            if "transaction_map_selector" in request.GET and request.GET["transaction_map_selector"] not in ["", "None"]
            else None
        )

        # get all associated transactions
        transactions = Transaction.objects.filter(mapping__id=transaction_map_id).all() if transaction_map_id else None

        # also return the transaction type selector and or transaction category selector

        context = {
            "transactions": transactions,
            "transaction_type_selected": transaction_type,
            "transaction_category_selected": transaction_category,
            "transaction_map_selected": transaction_map_id,
            "transaction_maps": transaction_maps,
            "transaction_type": TransactionType.objects.all(),
            "transaction_category": TransactionCategory.objects.all(),
            "form": TransactionMapForm(),
        }

        return render(request, "finance/transaction_maps.html", context)

    else:
        raise ValueError("Invalid request method.")


def update_transaction(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        # transaction id
        transaction_id = (
            int(request.POST["transaction_selector"])
            if "transaction_selector" in request.POST and request.POST["transaction_selector"] not in ["", "None"]
            else None
        )

        transaction_type_name = (
            str(request.POST["transaction_type_selector"])
            if "transaction_type_selector" in request.POST and request.POST["transaction_type_selector"] != ""
            else None
        )

        # get the existing transaction. if the type is different, create a new transaction mapping with the suitable
        #    type and map this transaction to the transaction mapping
        transaction = Transaction.objects.get(id=transaction_id)

        if transaction.mapping.type.name != transaction_type_name:

            # create a new transaction mapping
            new_map = TransactionMap.objects.create(
                name=transaction.mapping.name,
                description="Autogenerated Transaction Mapping",
                type=TransactionType.objects.get(name=transaction_type_name),
            )

            # map the transaction to the new map.
            transaction.mapping = new_map
            transaction.save()

        return HttpResponseRedirect("/finance/transaction")

    else:
        raise ValueError("Invalid request method.")


def import_transaction(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":

        start = datetime.strptime(request.POST["start"], "%Y-%m").date()
        end = datetime.strptime(request.POST["end"], "%Y-%m").date()

        import_transactions(start, end)

        return HttpResponseRedirect("/finance/transaction")

    else:
        raise ValueError("Invalid request method.")


def transaction(request: HttpRequest) -> HttpResponse:

    transactions = []
    if request.method == "GET":
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

    else:
        raise ValueError("Invalid request method.")
