from django.shortcuts import render
from apps.products.models import Product
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'pages/home.html', {'title':'Home'} )

def about(request):
    return render (request,'pages/about.html', {'title':'About'} )

def news(request):
    return render (request,'pages/news.html', {'title':'News'} )

def contact(request):
    return render (request,'pages/contact.html', {'title':'Contact'} )

def products(request):
    
    context = {
        'title':'Products',
        'products': Product.objects.all()
    }
    
    return render (request,'pages/products.html', context)
