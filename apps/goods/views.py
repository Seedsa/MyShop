from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters,viewsets,mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    #排序
    pagination_class = GoodsPagination
    #过滤、搜索、排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    #过滤
    filter_class = GoodsFilter
    #搜索
    search_fields = ('name','goods_desc','goods_brief')
    #排序
    ordering_fields = ('sold_num','add_time')

class CategoryViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
    List:
        商品分类列表数据
    """

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class =CategorySerializer
