from django.db.models.fields import EmailField
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
<<<<<<< HEAD
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message': message,
        }
        return render (request,'pages/contact.html', context)

    else:
        return render (request,'pages/contact.html', {'title':'Contact'} )
=======
    context = {
        'title':'Kontakt',
        'site_description': Site_description.objects.all(),
      }
    return render (request,'pages/contact.html', context )

    
  
>>>>>>> 5e82abbce38be29686c1d9f007be7999673ad524

