# Generated by Django 3.2.5 on 2021-08-17 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_description',
            name='about_description_1',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='about_description_2',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='contact_description_1',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='contact_description_2',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='home_description_1',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='home_description_2',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='news_description_1',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='news_description_2',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='product_description_1',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='site_description',
            name='product_description_2',
            field=models.TextField(blank=True, default='Wpisz opis w panelu admin', max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=400)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
