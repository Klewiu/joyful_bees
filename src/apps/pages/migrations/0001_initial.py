# Generated by Django 3.2.5 on 2021-08-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_description_1', models.TextField(default='Wpisz opis w panelu admin', max_length=1000)),
                ('about_description_2', models.TextField(default='Wpisz opis w panelu admin', max_length=500)),
                ('contact_description_1', models.TextField(default='Wpisz opis w panelu admin', max_length=1000)),
                ('contact_description_2', models.TextField(default='Wpisz opis w panelu admin', max_length=500)),
                ('home_description_1', models.TextField(default='Wpisz opis w panelu admin', max_length=1000)),
                ('home_description_2', models.TextField(default='Wpisz opis w panelu admin', max_length=500)),
                ('news_description_1', models.TextField(default='Wpisz opis w panelu admin', max_length=1000)),
                ('news_description_2', models.TextField(default='Wpisz opis w panelu admin', max_length=500)),
                ('product_description_1', models.TextField(default='Wpisz opis w panelu admin', max_length=1000)),
                ('product_description_2', models.TextField(default='Wpisz opis w panelu admin', max_length=500)),
            ],
        ),
    ]
