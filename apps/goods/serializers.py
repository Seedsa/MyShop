from rest_framework import serializers
from goods.models import Goods, GoodsCategory
import datetime


class CategorySerializer3(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = ('__all__')


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = ('__all__')


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = ('__all__')
