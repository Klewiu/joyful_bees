from django.urls import path
from . import views
from .views import ProductsView, ProductsDetailView


urlpatterns = [
    path('products/', views.products, name='page-products'),
    path('products_list/', ProductsView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products-detail'),
]