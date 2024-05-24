from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")