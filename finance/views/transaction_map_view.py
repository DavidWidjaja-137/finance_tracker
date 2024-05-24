from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from finance.models import TransactionMap, TransactionType, Transaction, TransactionCategory
from finance.models import TransactionMapForm


@method_decorator(login_required, name="dispatch")
class TransactionMapView(View):

    def get(self, request: HttpRequest):

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

    def post(self, request: HttpRequest):

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
