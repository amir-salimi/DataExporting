import django_filters
from .models import Building

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Building
        fields = ['name']