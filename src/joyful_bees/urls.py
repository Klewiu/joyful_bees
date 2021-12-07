"""joyful_bees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from joyful_bees import settings, sitemaps
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import security_txt
from .sitemaps import StaticViewsSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from apps.products.views import products

sitemaps={
    'sitemap': StaticViewsSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
    path('', include('apps.products.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.customers.urls')),
    path('', include('apps.newsletter.urls')),
    path(".well-known/security.txt", security_txt),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots.txt', lambda x: HttpResponse("Sitemap: https://www.pasiekaradosc.pl/sitemap.xml\nUser-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),name="favicon"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()