from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from .forms import NewsletterUserForm, MailMessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def newsletters(request):
    if request.method =='POST':
        form =NewsletterUserForm(request.POST)
        if form.is_valid():
            form.save() 
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
    if request.method =='POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Newsletter został wysłany do użytkowników')
            return redirect('profile')

    else:
        form = MailMessageForm()
    context = {
        'form' : form,
    }

    return render(request,'newsletter/runletter.html', context)