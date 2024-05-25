from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from finance.models import TransactionType, TransactionCategory


class TransactionTypeView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request: HttpRequest):

        context = {
            "transaction_types": TransactionType.objects.all(),
            "transaction_categories": TransactionCategory.objects.all(),
        }

        print(f"GET TransactionTypeView: {request.user} {request.user.username} {request.user.is_authenticated}")

        return render(request, "finance/transaction_types.html", context)

    def post(self, request: HttpRequest):

        # get the results of the post
        name = (
            str(request.POST["name"]) if "name" in request.POST and request.POST["name"] not in ["", "None"] else None
        )
        description = (
            str(request.POST["description"])
            if "description" in request.POST and request.POST["description"] not in ["", "None"]
            else None
        )
        category = (
            int(request.POST["category"])
            if "category" in request.POST and request.POST["category"] not in ["", "None"]
            else None
        )

        if name and description and category:
            TransactionType.objects.create(
                name=name,
                description=description,
                category=TransactionCategory.objects.get(id=category),
            )

        return HttpResponseRedirect("transaction_type")
