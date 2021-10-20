from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField (max_length=40, label=_(u'Imię'))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        