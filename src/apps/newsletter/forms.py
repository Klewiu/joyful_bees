from django import forms
from .models import NewsletterUser, MailMessage


class NewsletterUserForm (forms.ModelForm):
    email = forms.EmailField(label='Twój email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    
    
    class Meta:
        model = NewsletterUser
        fields = ['email']

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


