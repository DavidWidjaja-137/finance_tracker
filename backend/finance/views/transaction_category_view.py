from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views import View

from finance.models import TransactionCategory
from finance.models import TransactionCategoryForm


class TransactionCategoryView(View):
    form_class = TransactionCategoryForm
    initial = {"key": "value"}
    template_name = "finance/transaction_categories.html"

    def get(self, request: HttpRequest):

        transaction_categories = TransactionCategory.objects.all()
        context = {"transaction_categories": transaction_categories, "form": self.form_class(initial=self.initial)}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest):

        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/finance/transaction_category")
