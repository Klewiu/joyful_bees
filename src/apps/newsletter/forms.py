from django import forms
from .models import NewsletterUser, MailMessage

class NewsletterUserForm (forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']