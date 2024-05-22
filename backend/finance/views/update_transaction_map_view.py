from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View

from finance.models import TransactionMap, TransactionType


class UpdateTransactionMapView(View):

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
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
