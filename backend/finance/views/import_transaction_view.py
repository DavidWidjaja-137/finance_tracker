from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.views import View

from finance.importer.importer import import_transactions


class ImportTransactionView(View):

    def post(self, request: HttpRequest):

        start = datetime.strptime(request.POST["start"], "%Y-%m").date()
        end = datetime.strptime(request.POST["end"], "%Y-%m").date()

        import_transactions(start, end)

        return HttpResponseRedirect("/finance/transaction")
