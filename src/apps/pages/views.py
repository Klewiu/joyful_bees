from django.db.models.fields import EmailField
from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'pages/home.html', {'title':'Home'} )

def about(request):
    return render (request,'pages/about.html', {'title':'About'} )

def news(request):
    return render (request,'pages/news.html', {'title':'News'} )

def contact(request):
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

