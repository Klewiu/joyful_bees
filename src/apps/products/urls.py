from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='page-products'),
    path('products_list/', views.products_list, name='page-products_list'),
]