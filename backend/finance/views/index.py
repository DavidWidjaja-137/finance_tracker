from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name="dispatch")
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect("/finance/transaction")
