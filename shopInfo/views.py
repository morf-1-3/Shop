from django.shortcuts import render
from django.http import HttpRequest
from .models import *
# from ..catalog.models import Category
from catalog.models import Category, Product
# Create your views here.
def index(request: HttpRequest):
    categories = Category.objects.all()[:4]
    products = Product.objects.all()[:4]
    context={
        "categories": categories,
        "products": products
    }
    return render(request,"shopInfo/index.html",context)



def contact(request: HttpRequest):
    return render(request, "shopInfo/contact.html")


def about(request: HttpRequest):
    shopInfo = ShopInfo.objects.first()
    description = shopInfo.descriptions
    context = {
        "description": description
    }
    return render(request, "shopInfo/about.html",context)