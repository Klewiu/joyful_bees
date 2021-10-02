import django_filters
from .models import * # gwiazdka importuje wszystkie modele

class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Wyszukaj klienta po nazwie:',lookup_expr='contains')  
    class Meta:
        model = Customer
        fields = ['name']

