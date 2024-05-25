from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


from finance.models import TransactionCategory


class TransactionCategoryView(LoginRequiredMixin, View):

    def get(self, request: HttpRequest):

        transaction_categories = TransactionCategory.objects.all()
        context = {
            "transaction_categories": transaction_categories,
        }

        return render(request, "finance/transaction_categories.html", context)

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

        if name and description:
            TransactionCategory.objects.create(name=name, description=description)

        return HttpResponseRedirect("transaction_category")
