from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializer import *
import datetime




@api_view(['GET' ])
def shoplist(request):
    """
    List all shop in a given country
    """
    if request.method == 'GET':
        shoplist = Shop.objects.all()
        serializer = ShopSerializer(shoplist,many=True)
        return Response(serializer.data)

@api_view(['GET' ])
def companylist(request):
    """
    List all shop in a given country
    """
    if request.method == 'GET':
        company = request.GET.get('c')
        companylist = Company.objects.filter(id=company)
        serializer = CompanySerializer(companylist,many=True)
        return Response(serializer.data)



@api_view(['GET', ])
def shop_country_list(request):
    """
    List all shop in a given country
    """
    if request.method == 'GET':
        #country = request.get('country')
        shoplist = Shop.objects.filter(region__country_id='Mauritius')
        serializer = ShopSerializer(shoplist,many=True)
        return Response(serializer.data)


@api_view(['GET',])
def shop_region_list(request):
    """
    List all shop in a given region
    """
    if request.method == 'GET':
        #region = request.get('region')
        shoplist = Shop.objects.filter(region__id='port-louis')
        serializer = ShopSerializer(shoplist,many=True)
        return Response(serializer.data)



@api_view(['GET',])
def shop_product_list(request):
    """
    List all shop with a given product
    """
    if request.method == 'GET':
        country = request.get('country')
        shoplist = Shop.objects.filter(region__country=country)
        serializer = ShopSerializer(shoplist,many=True)
        return Response(serializer.data)




@api_view(['GET'])
def shop_product_region(request):
    """
    List all shop in a given country
    """
    if request.method == 'GET':
        region = request.get('region')
        product = request.ge('product')
        shoplist = Shop.objects.filter(region__id=region).filter(product__name__contains=product)
        serializer = ShopSerializer(shoplist)
        return Response(serializer.data)



@api_view(['GET'])
def shop_region_company(request):
    """
    List all shop in a given region and product
    """
    if request.method == 'GET':
        country = request.get('country')
        product = request.ge('product')
        shoplist = Shop.objects.filter(region__country=country).filter(product__name__contains=product)
        serializer = ShopSerializer(shoplist,many=True)
        return Response(serializer.data)




@api_view(['GET'])
def product_list(request):
    """
    List all products for a given company
    """
    if request.method == 'GET':
        company = request.GET.get('c')
        products= Product.objects.filter(company__id=company)

        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_in_shop_list_date(request):
    """
    List all product for a for given region in  given date
    """
    if request.method == 'GET':
        #product = request.get('product')
        #region = request.get('region')
        #time = request.get('time')
        products= ProductInShop.objects.filter(product_id='Permagloze', shop__region__id='port-louis').filter(timestamp=datetime.date(2019,10,28))
        serializer = ProductInShopSerializer(products,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def products_in_shops_list(request):
    """
    List all product for a for given region in  given range
    """
    if request.method == 'GET':
        product = request.get('product')
        region = request.get('region')
        start_date = datetime.date(request.get('start_date'))
        end_date = datetime.date(request.get('end_date'))
        products= ProductInShop.objects.filter(shop__region__id=region).\
            filter(timestamp__range=(start_date, end_date))
        serializer = ProductInShopSerializer(products,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def product_in_shop_list_range(request):
    """
    List all product for a for given region in  given range
    """
    if request.method == 'GET':
        product = request.get('product')
        region = request.get('region')
        start_date = datetime.date(request.get('start_date'))
        end_date = datetime.date(request.get('end_date'))
        productinshop= ProductInShop.objects.filter(product_id=product, shop__region__id=region).\
            filter(timestamp__range=(start_date, end_date))
        serializer = ProductInShopSerializer(productinshop,many=True)
        return Response(serializer.data)