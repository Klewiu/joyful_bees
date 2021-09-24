from django import forms
from .models import NewsletterUser, MailMessage

class NewsletterUserForm (forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = NewsletterUser
        fields = ['email']

    def clean_email (self, *args, **kwargs):
        email= self.cleaned_data.get('email')
        qs= NewsletterUser.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Ten email już istnieje w naszej bazie")

        return email

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'


