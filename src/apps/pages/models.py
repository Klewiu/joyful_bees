from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=150, verbose_name='tytuł')
    content = models.TextField(max_length=400, verbose_name = 'treść')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " / " + str(self.author)

    def get_absolute_url(self):
        return reverse('page-news')



class Site_description (models.Model):
    about_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000, null=True, blank=True)
    about_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500, null=True, blank=True)
    contact_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000, null=True, blank=True)
    contact_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500, null=True, blank=True)
    home_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000, null=True, blank=True)
    home_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500, null=True, blank=True)
    news_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000, null=True, blank=True)
    news_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500, null=True, blank=True)
    product_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000, null=True, blank=True)
    product_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500, null=True, blank=True)

