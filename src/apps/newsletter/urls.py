from django.urls import path
from . import views

urlpatterns = [
path ('newsletter/', views.newsletters, name='newsletter'),
path ('runletter/', views.runletter, name='runletter'),
path('confirm/', views.confirm, name='confirm'),
path('delete/', views.delete, name='delete'),
]