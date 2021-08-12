from django.shortcuts import render
from apps.products.models import Product
from apps.pages.models import Site_description

# Create your views here.

def products(request):
    
    context = {
        'title':'Produkty',
        'products': Product.objects.all(),
        'site_description': Site_description.objects.all(),
    }
    
    return render (request,'products/products.html', context)
