from django.shortcuts import render
from apps.customers.models import Customer

# Create your views here.

def customers (request):
    context = {
        'customers': Customer.objects.all(),
    }
    return render(request, 'customers.html', context)
