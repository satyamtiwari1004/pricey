from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
def saveData(productDict):
    product=Product(
        title_string=productDict.get("title_string"),
        mrp=productDict.get("mrp"),
        discountedPrice=productDict.get("discountedPrice"),
        rating=productDict.get("rating"),
        review_count=productDict.get("review_count"),
        available=productDict.get("available"),
        ram=productDict.get("RAM"),
        os=productDict.get("OS"),
        importer=productDict.get("Manufacturer")
    )
    product.save()

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
