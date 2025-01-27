from django.shortcuts import render
from django.http import HttpRequest
from .models import *
# Create your views here.
def index(request: HttpRequest):

    return render(request,"shopInfo/index.html")



def contact(request: HttpRequest):
    return render(request, "shopInfo/contact.html")


def about(request: HttpRequest):
    shopInfo = ShopInfo.objects.first()
    description = shopInfo.descriptions
    context = {
        "description": description
    }
    return render(request, "shopInfo/about.html",context)