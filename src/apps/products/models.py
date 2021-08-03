from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(default="Add description here", max_length=200)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    price = models.FloatField(help_text=' PLN')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def clean(self):

        if not self.image:
            raise ValidationError("No image!")
        else:
            w, h = get_image_dimensions(self.image)
            if w != 450:
                raise ValidationError("The image is %i pixel wide. It's supposed to be 450px" % w)
            if h != 450:
                raise ValidationError("The image is %i pixel high. It's supposed to be 450px" % h)

    def __str__(self):
        return f"{self.name}"





