from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.customers.models import Customer
from .forms import UserRegisterForm
from apps.products.models import Product


# Create your views here.
@login_required
def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono konto dla {username}, zaloguj się')
            return redirect ('login') #redirect affter successful registration

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile (request):

    return render(request, 'users/profile.html')

