from django.urls import path
from . import views
from .views import CustomersView, CustomersDetailView, CustomersCreateView, CustomersUpdateView, CustomersDeleteView


urlpatterns = [
    path('manage_cusomers/', CustomersView.as_view(), name='customers-view'),
    path('customers/<int:pk>/', CustomersDetailView.as_view(), name='customers-detail'),
    path('customers/new/', CustomersCreateView.as_view(), name='customers-create'),
    path('customers/<int:pk>/update/', CustomersUpdateView.as_view(), name='customers-update'),
    path('customers/<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers-delete'),

]