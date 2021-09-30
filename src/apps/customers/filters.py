from django.db.models import fields
import django_filters
from django_filters.utils import verbose_field_name
import django_filters as filters

from .models import * # gwiazdka importuje wszystkie modele

class OrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Wyszukaj klienta po nazwie:',lookup_expr='contains')  
    class Meta:
        model = Customer
        fields = ['name']

