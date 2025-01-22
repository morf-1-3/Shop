from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Cart,ProductInCart
from catalog.models import Product
# Create your views here.

def main(request:HttpRequest):
    products = Product.objects.all()
    context = {
        "products": products
    }
    response = render(request,"cart/index.html")
    response, cart = Cart.get_cart(request,response)
    return response 

def get_cart(request: HttpRequest):

    cart = Cart.get_cart(request)
    # if "cart_id" not in request.COOKIES:
        
    #     request.COOKIES["cart_id"] = cart.cart_id 
    
    response = render(request,"cart/includes/cart.html",{'products': cart.products.all()})
    if "cart_id" not in response.cookies and cart.cart_id:
        response.set_cookie('cart_id', cart.cart_id)
    
    return response

def add_to_cart(request:HttpRequest,product_id:int):
    if request.method == "POST":
        cart = Cart.get_cart(request)
        
        products = cart.products.all()
        if(products.filter(product__id=product_id)).exists():
            product = products.get(product__id=product_id)
            if product.count < 9:
                product.count += 1
                product.save()
        else:
            ProductInCart.objects.create(cart=cart, product = Product.objects.get(id=product_id))

    return HttpResponse(200)


def plus_count_cart(request:HttpRequest,product_id:int):
    if request.method == "POST":
        cart = Cart.get_cart(request)
        products = cart.products.all()
        product = products.get(id=product_id)
        if product.count < 9:
            product.count += 1
            product.save()
        
    return HttpResponse(200)

def minus_count_cart(request:HttpRequest,product_id:int):
    if request.method == "POST":
        cart = Cart.get_cart(request)
        products = cart.products.all()
        product = products.get(id=product_id)
        if product.count > 1:
            product.count -= 1
            product.save()
        
    return HttpResponse(200)

def remove_count_cart(request:HttpRequest,product_id:int):
    if request.method == "POST":
        cart = Cart.get_cart(request)
        products = cart.products.all()
        product = products.get(id=product_id)
        product.delete()
        
    return HttpResponse(200)

# def redirect_to_order(request:HttpRequest)
#     cart = Cart.get_cart(request)
#     products = cart.products.all()

#     context = {
#         "products": products
#     }
