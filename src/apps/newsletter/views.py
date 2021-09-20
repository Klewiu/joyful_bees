from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from .forms import NewsletterUserForm
from django.contrib import messages

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