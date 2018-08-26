from django_filters import rest_framework as filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(field_name='shop_price', lookup_expr='gt')
    pricemax = filters.NumberFilter(field_name='shop_price', lookup_expr='lt')
    # 模糊查询
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = filters.NumberFilter(method='top_category_filter')

    #第一类过滤
    def top_category_filter(self, queryset, field_name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
