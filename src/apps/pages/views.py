from django.shortcuts import render
from apps.pages.models import Site_description
from django.core.mail import send_mail
from django.contrib import messages

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
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #sending emial through contact form
        if message_name and message_email and message:
          send_mail(
            f'Formularz Kontaktowy, wiadomość od {message_name}',
            f'Wiadomość ze strony Pasieka Radość od {message_email}: {message}',
            message_email,
            ['tomekklewicki@wp.pl'],)
          messages.success(request, f'Dziękujemy za kontakt {message_name}, Twój email został wysłany')
        else:
          messages.warning(request, 'Wypełnij wszystkie pola formularza przed wysłaniem')


        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message': message,
            'title':'Kontakt',
            'site_description': Site_description.objects.all()
        }
        return render (request,'pages/contact.html', context)

    else:
        context = {
        'title':'Kontakt',
        'site_description': Site_description.objects.all(),
      }
        return render (request,'pages/contact.html', context)




    
  

