from rest_framework import serializers
from main.models import *



class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name', 'central_lats', 'central_longs']


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['id', 'name', 'country', 'central_lats', 'central_longs']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id', 'name', 'region', 'country']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'size', 'metric','company']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'region', 'lat','long']


class ProductInShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInShop
        fields = ['product', 'shop', 'date', 'available','price','shelf','facing']


