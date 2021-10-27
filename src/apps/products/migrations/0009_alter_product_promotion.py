# Generated by Django 3.2.5 on 2021-10-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotion',
            field=models.FloatField(blank=True, choices=[('no_promo', 0), ('5%', 5), ('10%', 10), ('15%', 15), ('20%', 20), ('30%', 30), ('40%', 40), ('50%', 50)], default=0, verbose_name='Promocja w %'),
        ),
    ]
