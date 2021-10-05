from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from sendgrid.helpers.mail.bcc_email import Bcc
from .forms import NewsletterUserForm, MailMessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Content, To
from .models import NewsletterUser
from django import forms
import pandas as pd
# Create your views here.

def newsletters(request):
    if request.method =='POST':
        form =NewsletterUserForm(request.POST)
        if form.is_valid():
            form.save() 
            email= form.cleaned_data.get('email')
            messages.success(request, f'Dziękujemy za zapisanie adresu {email} do naszego newslettera!')
            return redirect('/')
            
    else:
        form =NewsletterUserForm()
    context = {
        'title':'Newsletter',
        'form': form,
    }
    return render (request, 'newsletter/newsletter.html', context)




@login_required
def runletter(request):
    # GETTING QUERYSET FOR EMAILS    
    qs = NewsletterUser.objects.all().values()
    df = pd.DataFrame(qs)
    emails=(list(df.email))

    if request.method =='POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Newsletter został wysłany do użytkowników')
            message = Mail(
                from_email='pasiekaradosc@gmail.com',
                to_emails= emails,
                is_multiple=True,
                subject= form.cleaned_data.get('title'),
                html_content= form.cleaned_data.get('message'))
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

    

