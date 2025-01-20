from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import *
# Create your views here.


def show_category(request:HttpRequest, category:str):
    context = {}
    if request.method == "GET":
        categories = Category.objects.all()
        if categories.filter(name_en__iexact=category).exists():
            my_category = categories.get(name_en__iexact=category)
            products = my_category.products.all()
            context["products"] = products
            return render(request, 'catalog/category.html',context)
        else:
            return HttpResponseNotFound()

def show_item(request:HttpRequest, category:str, item_id:int):
    context = {}

    if request.method == "GET":
        if Product.objects.filter(id=item_id).exists(): 
            product = Product.objects.get(id=item_id)
            context["product"] = product
            return render(request,"catalog/product.html",context)

        else:
            return HttpResponseNotFound()


def show_items(request:HttpRequest):
    context = {}

    if request.method == "GET":
        if Product.objects.all().exists(): 
            products = Product.objects.all()
            context["products"] = products
            return render(request,"catalog/products.html",context)

        else:
            return HttpResponseNotFound()
