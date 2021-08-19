from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    name =  models.CharField(max_length=50, help_text="Podaj imię i nazwisko lub unikalną nazwę klienta")
    email = models.CharField(max_length=50)
    tel = PhoneNumberField()
    address = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def email_str():
        email_string = str(Customer.email)
        return email_string