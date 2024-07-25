import django_filters
from Building.models import Building

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Building
        fields = ['name']