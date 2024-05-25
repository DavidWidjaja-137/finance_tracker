from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "finance/index.html")