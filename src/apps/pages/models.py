from django.db import models

class Site_description (models.Model):
    about_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000)
    about_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500)
    contact_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000)
    contact_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500)
    home_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000)
    home_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500)
    news_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000)
    news_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500)
    product_description_1 = models.TextField(default="Wpisz opis w panelu admin", max_length=1000)
    product_description_2 = models.TextField(default="Wpisz opis w panelu admin", max_length=500)
