from django_filters import rest_framework as filters

from apps.my_cars.models import CarModel


class CarFilter(filters.FilterSet):
    class Meta:
        model = CarModel
        fields = {
            'brand': ('icontains', 'istartswith', 'iendswith'),
            'year': ('lt', 'lte', 'gt', 'gte'),
            'price': ('lt', 'lte', 'gt', 'gte'),
            'engine_volume': ('lt', 'lte', 'gt', 'gte')
        }

    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            'year',
            'price',
            'engine_volume'
        )
    )
