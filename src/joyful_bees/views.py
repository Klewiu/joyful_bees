from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def security_txt(request):
    lines = [
        "Contact: kuba.klewicki@gmail.com",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")