from django.shortcuts import render
from apps.products.models import Product
from apps.pages.models import Site_description
from django.shortcuts import redirect

# Create your views here.

def products(request):
    
    context = {
        'title':'Produkty',
        'products': Product.objects.all(),
        'site_description': Site_description.objects.all(),
    }
    return render (request,'products/products.html', context)

def products_list(request):
    
    context = {
        'title':'Admin - Lista produktów',
        'products': Product.objects.all(),
    }

    if request.user.is_authenticated and request.user.is_superuser:
        return render (request,'products/products_list.html', context)
    else:
        return redirect('page-home')