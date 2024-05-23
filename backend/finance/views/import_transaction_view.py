from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from finance.importer.importer import import_transactions


@method_decorator(login_required, name="dispatch")
class ImportTransactionView(View):

    def post(self, request: HttpRequest):

        start = datetime.strptime(request.POST["start"], "%Y-%m").date()
        end = datetime.strptime(request.POST["end"], "%Y-%m").date()

        import_transactions(start, end, request.user)

        return HttpResponseRedirect("/finance/transaction")
