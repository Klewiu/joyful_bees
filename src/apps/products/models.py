from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nazwa produktu')
    description = models.TextField(max_length=500, verbose_name='Opis produktu')
    image = models.ImageField(upload_to='products', default='no_picture.png',verbose_name='Zdjęcie produktu', help_text="ZDJĘCIE MIUSI MIEĆ 450x450 px!")
    price = models.FloatField(help_text=' PLN', verbose_name='Cena produktu')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    availability = models.IntegerField(default=1, verbose_name='Dostępność produktu')

    def get_absolute_url(self):
        return reverse('products-list')

    def clean(self):

        if not self.image:
            raise ValidationError("No image!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 450:
                raise ValidationError("Obraz jest o szerokości %i pixeli. Obraz musi mieć 450 x 450 px" % w)
            if h != 450:
                raise ValidationError("Obraz jest o wysokości %i pixeli. Obraz musi mieć 450 x 450 px" % h)

    def __str__(self):
        return f"{self.name}"