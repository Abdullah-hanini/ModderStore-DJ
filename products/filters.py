import django_filters
from .models import Products

class GamesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['title']