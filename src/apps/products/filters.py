import django_filters

from .models import * # gwiazdka importuje wszystkie modele

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Wyszukaj produkt po nazwie:',lookup_expr='contains')  
    class Meta:
        model = Product
        fields = ['name']