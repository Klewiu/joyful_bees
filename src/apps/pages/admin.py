from django.contrib import admin
from apps.pages.models import Site_description
from .models import Post

# Register your models here.
admin.site.register(Site_description)
admin.site.register(Post)