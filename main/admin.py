from django.contrib import admin
from .models import Shop, ProductInShop, Product, Region,Country,Company
from django.utils.translation import ugettext_lazy
from import_export import  resources
from import_export.admin import ImportExportModelAdmin



admin.site.site_title = ugettext_lazy('Rwazi')
admin.site.site_header = ugettext_lazy('Rwazi')
admin.site.index_title = ugettext_lazy('Rwazi')


class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop
class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ('shop')

class ProductInShopResource(resources.ModelResource):
    class Meta:
        model = ProductInShop

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region

class CountryResource(resources.ModelResource):
    class Meta:
        model =  Country

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource
    list_display = ('id','name','location')
    search_fields =('name',)

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    resource_class = ShopResource
    list_display = ('id','name','region','lat','long')
    search_fields =('name',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('id','name','size','company')
    search_fields = ('name', 'company')


@admin.register(ProductInShop)
class ProductInShopAdmin(ImportExportModelAdmin):
    resource_class = ProductInShopResource
    list_display = ("get_shop_region",'shop','product','date','available','price','shelf','facing')
    search_fields = ['shop__name','product__name', 'shop__region__name','product__company__name']
    list_filter = ['product__company__name',]










@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display =  ('id','name', 'country')
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)