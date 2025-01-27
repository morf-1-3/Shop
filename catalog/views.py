from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import *
from django.db.models import Max,Min
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
            filter_categories = request.GET.getlist("filter_categories")
            filter_min_price = request.GET.get("price_min")
            filter_max_price = request.GET.get("price_max")
            if(filter_categories or filter_max_price or filter_min_price):
                if filter_categories:
                    products = products.filter(category__name_en__in = filter_categories)
                if filter_max_price:                    
                    products = products.filter(price__lte = filter_max_price)
                if filter_min_price:
                    products = products.filter(price__gte = filter_min_price)
            
            context["products"] = products

            price_range = products.aggregate(
                min_price = Min("price"),
                max_price = Max("price")
            )
            context["min_price"] = price_range["min_price"]
            context["max_price"] = price_range["max_price"]
            return render(request,"catalog/products.html",context)

        else:
            return HttpResponseNotFound()
