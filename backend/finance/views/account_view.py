from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from finance.models import Account
from finance.models import AccountForm


@method_decorator(login_required, name="dispatch")
class AccountView(View):
    form_class = AccountForm
    initial = {"key": "value"}
    template_name = "finance/accounts.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        all_accounts = Account.objects.all()
        context = {"all_accounts": all_accounts, "form": self.form_class(initial=self.initial)}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/finance/transaction_account")
