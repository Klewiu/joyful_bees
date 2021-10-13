from django.db import models
from django.db.models.constraints import UniqueConstraint


# Create your models here.

class NewsletterUser (models.Model):
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"




class MailMessage (models.Model):
    title = models.CharField (max_length=100, null=True)
    message = models.TextField()
    

    def __str__(self):
        return self.title

    