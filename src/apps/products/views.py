from django.shortcuts import render
from apps.products.models import Product
# Create your views here.

def products(request):
    
    context = {
        'title':'Products',
        'products': Product.objects.all()
    }
    
    return render (request,'products/products.html', context)
