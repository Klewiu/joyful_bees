from django.shortcuts import render
from apps.customers.models import Customer
from django.shortcuts import redirect

# Create your views here.


def customers (request):
    context = {
        'title':'Admin - Baza klientów',
        'customers': Customer.objects.all(),
    }

    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'customers/customers.html', context)
    else:
        return redirect('page-home')

