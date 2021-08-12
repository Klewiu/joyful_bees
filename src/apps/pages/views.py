from django.shortcuts import render
from apps.pages.models import Site_description
# from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'title':'Strona główna',
        'site_description': Site_description.objects.all(),
      }

    return render (request,'pages/home.html', context)

def about(request):
    context = {
        'title':'O nas',
        'site_description': Site_description.objects.all(),
      }
    return render (request,'pages/about.html', context )

def news(request):
    context = {
        'title':'Aktualności',
        'site_description': Site_description.objects.all(),
      }
    return render (request,'pages/news.html', context)

def contact(request):
    context = {
        'title':'Kontakt',
        'site_description': Site_description.objects.all(),
      }
    return render (request,'pages/contact.html', context )

    
  

