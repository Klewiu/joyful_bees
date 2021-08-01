from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default="Add description here")
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text=' PLN')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"