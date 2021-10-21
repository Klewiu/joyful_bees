from django.urls import path
from . import views
from .views import UserNewsletterView


urlpatterns = [
path('newsletter_user_list/', UserNewsletterView.as_view(), name='newsletter_user_list-view'),
path ('newsletter/', views.newsletters, name='newsletter'),
path ('runletter/', views.runletter, name='runletter'),
path('confirm/', views.confirm, name='confirm'),
path('delete/', views.delete, name='delete'),
]