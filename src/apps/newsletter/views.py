from django.shortcuts import render
from .forms import NewsletterUserForm

# Create your views here.

def newsletters(request):
    
    form =NewsletterUserForm()
    context = {
        'form': form,
    }
    return render (request, 'newsletter/newsletter.html', context)