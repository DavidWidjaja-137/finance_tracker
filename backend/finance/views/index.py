from django.http import HttpResponse, HttpRequest, HttpResponseRedirect


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect("/finance/transaction")
