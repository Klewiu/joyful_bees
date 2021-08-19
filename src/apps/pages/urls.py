from django.urls import path
from . import views
from .views import NewsView, NewsDetailView, NewsCreateView

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('news/', NewsView.as_view(), name='page-news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='post-detail'),
    path('news/new/', NewsCreateView.as_view(), name='news-create'),
    path('contact/', views.contact, name='page-contact'),
] 