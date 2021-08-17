from django.db import models



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
