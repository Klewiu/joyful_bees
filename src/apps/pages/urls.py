from django.urls import path
from . import views
from .views import NewsView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView, faq

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
    path('foto/', views.foto, name='page-foto'),
    path('news/', NewsView.as_view(), name='page-news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='post-detail'),
    path('news/new/', NewsCreateView.as_view(), name='news-create'),
    path('contact/', views.contact, name='page-contact'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='post-update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='post-delete'),
    path('privacy/',views.privacy, name='page-privacy'),
    path('terms/',views.terms, name='page-terms'),
    path('faq/',views.faq, name='page-faq'),
    path('info/', views.info, name ='page-info'),
   
] 