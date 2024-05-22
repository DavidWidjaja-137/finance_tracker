from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View

from finance.models import TransactionType
from finance.models import TransactionTypeForm


class TransactionTypeView(View):
    form_class = TransactionTypeForm
    initial = {"key": "value"}
    template_name = "finance/transaction_types.html"

    def get(self, request: HttpRequest):

        transaction_types = TransactionType.objects.all()
        context = {"transaction_types": transaction_types, "form": self.form_class(initial=self.initial)}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/finance/transaction_type")
