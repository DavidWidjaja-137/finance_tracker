import os
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from finance.models import Account
from finance.s3_util import s3_util


@method_decorator(login_required, name="dispatch")
class TransactionFileView(View):

    def get(self, request: HttpRequest):

        # check how many files are in the account
        filter_start = (
            datetime.strptime(request.GET["filter_start"], "%Y-%m").date() if "filter_start" in request.GET else None
        )
        filter_end = (
            datetime.strptime(request.GET["filter_end"], "%Y-%m").date() if "filter_end" in request.GET else None
        )
        account = (
            str(request.GET["transaction_account_selector"]) if "transaction_account_selector" in request.GET else None
        )

        # check on S3 how many files are there
        keys = []
        #if account:
        #    keys = s3_util.get_s3_filenames(os.path.join("data", request.user.username, account))
        #else:
        #    keys = []

        # filter the files according to the date range
        filtered_keys = [
            k
            for k in keys
            if filter_start <= datetime.strptime(os.path.basename(k).split(".")[0], "%Y-%m-%d").date() < filter_end
        ]

        context = {"transaction_accounts": Account.objects.all(), "transaction_files": filtered_keys}

        return render(request, "finance/transaction_file_downloader.html", context)

    def post(self, request: HttpRequest):

        file_date = (
            datetime.strptime(request.POST["file_date"], "%Y-%m").date().isoformat()
            if "file_date" in request.POST
            else None
        )

        account = (
            str(request.POST["transaction_account_selector"])
            if "transaction_account_selector" in request.POST
            else None
        )

        if file_date and account and request.FILES and request.FILES["file_upload"]:
            key = os.path.join("data", request.user.username, account, file_date + ".csv")
            s3_util.bucket.upload_fileobj(request.FILES["file_upload"].file, key)

        return HttpResponseRedirect("/finance/transaction_file_downloader")
