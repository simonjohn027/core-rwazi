from django.db import models
from .choices import SHOP_CHOICES, PRODUCT_CHOICES, METRIC_TYPE


class Country(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    central_lat = models.FloatField()
    central_long = models.FloatField()

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Region(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    central_lat = models.FloatField()
    central_long = models.FloatField()

    def __str__(self):
        return self.name


class Shop(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    type = models.CharField(choices=SHOP_CHOICES,default='convinience', max_length=200)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500,verbose_name="Company Name")
    location = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.CharField(max_length=1000, primary_key=True)
    name = models.CharField(max_length=1000, blank=False, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.CharField(choices=PRODUCT_CHOICES,max_length=500, default='fmcg')
    size = models.FloatField(blank=True, default=100, null=False)
    metric = models.CharField(choices=METRIC_TYPE, max_length=100, default="Gram", null=False, blank=True)
    shop = models.ManyToManyField(Shop, through='ProductInShop', related_name='product')

    def __str__(self):
        return self.name


class ProductInShop(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, related_name='product_in_shop')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='product_in_shop')
    available = models.BooleanField()
    price = models.FloatField()
    shelf = models.IntegerField()
    facing = models.IntegerField()
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s - %s ' % (self.shop, self.product)

    def get_shop_region(self):
        return self.shop.region

    get_shop_region.short_description = "Region"
