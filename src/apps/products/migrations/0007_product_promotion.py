# Generated by Django 3.2.5 on 2021-10-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promotion',
            field=models.CharField(choices=[('no_promo', 0), ('5%', 5), ('10%', 10)], default='no_promo', max_length=50),
        ),
    ]
