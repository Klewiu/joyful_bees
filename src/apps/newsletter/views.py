from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from sendgrid.helpers.mail.bcc_email import Bcc
from django.http import HttpResponse
from .forms import NewsletterUserForm, MailMessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Content, To
from .models import NewsletterUser
from django import forms
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import random
from sendgrid import SendGridAPIClient
from django.db import IntegrityError
from django.views.generic import ListView
from apps.products.views import AdminStaffRequiredMixin

# Create your views here.

#!REGISTER CURRENT HOST!
host = ['http://127.0.0.1:8000/']

# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)



@csrf_exempt
def newsletters(request):
    if request.method == 'POST':
        sub = NewsletterUser(email=request.POST['email'], conf_num=random_digits())
        try:
            sub.save()
            message = Mail(
                from_email='pasiekaradosc@gmail.com',
                to_emails=sub.email,
                subject='Potwierdzenie Adresu Email w Newsletterze Pasieka Radość',
                html_content= "<h1>Dziękujemy za zapisanie się do newslettera Pasieka Radość!<h1> \
                    <h2>Od teraz będziemy mogli przesyłać Ci najświeższe informacje z naszej pasieki, potwierdź rejestrację newslettera.</h2> \
                    <h2><a href='{}confirm/?email={}&conf_num={}'> Kliknij w ten link</a>.<h2>".format(request.build_absolute_uri(host),
                                                        sub.email,
                                                        sub.conf_num))
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)
            return render(request, 'newsletter/newsletter.html', {'email': sub.email, 'action': 'wysłano', 'form': NewsletterUserForm()})
        except IntegrityError:
            messages.error(request, f'Twój email {sub.email} został już zarejestrowany w naszym newsletterze lub czeka na potwierdzenie')
            return render(request, 'newsletter/newsletter.html', {'form': NewsletterUserForm()})
    else:
        return render(request, 'newsletter/newsletter.html', {'form': NewsletterUserForm()})

def confirm(request):
    sub = NewsletterUser.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        messages.success(request, f'Dziękujemy za zapisanie adresu email do naszego newslettera!')
        return render(request, 'pages/home.html' , {'email': sub.email, 'action': 'confirmed'})     
        
    else:
        return render(request, 'newsletter/newsletter.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = NewsletterUser.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        messages.error(request, f'Twój email został wypisany z naszej bazy danych!')
        return render(request, 'pages/home.html', {'email': sub.email, 'action': 'unsubscribed'})
        
    else:
        return render(request, 'newsletter/newsletter.html', {'email': sub.email, 'action': 'denied'})


@login_required
def runletter(request):
    # GETTING QUERYSET FOR CONFIRMED EMAILS    
    qs = NewsletterUser.objects.filter(confirmed=True)
  

    if request.method =='POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Newsletter został wysłany do użytkowników')
            for sub in qs:
                message = Mail(
                    from_email='pasiekaradosc@gmail.com',
                    to_emails= sub.email,
                    is_multiple=True,
                    subject= form.cleaned_data.get('title'),
                    html_content= form.cleaned_data.get('message')+(
                        '<br><br><hr><p><a href="{}delete/?email={}&conf_num={}">Wypisz mnie z Newslettera!</a></p>').format(request.build_absolute_uri(host),
                            sub.email,
                            sub.conf_num))
                try:
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                    response = sg.send(message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
                except Exception as e:
                    print(e)

            return redirect('profile')


    else:
        form = MailMessageForm()
    context = {
        'form' : form,
    }

    return render(request,'newsletter/runletter.html', context)

class UserNewsletterView (AdminStaffRequiredMixin, ListView):
    model=NewsletterUser
    template_name = 'newsletter/newsletter_user_list.html'
 

