from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from cart.models import *
from users.models import *
from .services.nova_posta import *
from django.http import JsonResponse

# Create your views here.
def checkout(request: HttpRequest):
    if request.method == "GET":
        cart = Cart.get_cart(request)
        
        
        context = {
            "cart": cart
        }
        return render(request,'orders/checkout_order.html',context)
    if request.method == "POST":
        context = {}
        cart = Cart.get_cart(request)
        context["cart"] = cart

        first_name = request.POST["user_first_name"]
        last_name = request.POST["user_last_name"]
        phone_number = request.POST["phone_number"]
        warehouse_ref = request.POST["id-warehouse"]
        context["first_name"] = first_name
        context["last_name"] = last_name
        context["phone_number"] = phone_number
        if(first_name and last_name and phone_number and warehouse_ref):
            if 2<=len(first_name)<30 and 2<=len(last_name)<30:
                if 10<=len(phone_number) <=13:
                    if True:
                        order = Order.objects.create()
                        reveiver = Receiver.objects.create(
                            first_name = first_name,
                            last_name = last_name,
                            phone_number= phone_number,
                            order = order,
                            ref_warehouse = warehouse_ref
                            )
                        for product in cart.products.all():
                            ProductInOrder.objects.create(
                                product = product.product,
                                order = order,
                                count = product.count
                            )
                    return render(request,"orders/success.html")
                else:
                    context["error"] = "Введіть коректно телефон"
                    # return render(request,'orders/checkout_order.html',context)
                
            else:
                context["error"] = "Введіть коректно ім'я та прізвище"
                # return render(request,'orders/checkout_order.html',context)

        else:
            
            context["error"] = "Введіть всі поля"
        return render(request,'orders/checkout_order.html',context)


        if request.user.is_authenticated:
            pass
            
        else:
            pass

def make_order(request:HttpRequest):
    if request.method == "POST":
        pass
       

def show_seltements(request:HttpRequest,search_str: str = ""):
    if search_str:
        settlements = get_settlements(search_str)
        context = {"main_sities" : settlements}
    else:
        context = {"main_sities": main_sities}

    html = render(request,"orders/dropdown_cities.html",context).content.decode('utf-8')
    # return render(request,"orders/dropdown_cities.html",context)
    return JsonResponse({"html": html})

def show_warehouses(request: HttpRequest, ref: str, search_str: str = ""):
    if search_str:
        warehouses = get_warehouses(ref,search_str)
        context = {"main_sities" : warehouses}
    else:
        warehouses = get_warehouses(ref)
        context = {"main_sities" : warehouses}
    html = render(request,"orders/dropdown_cities.html",context).content.decode('utf-8')
    return JsonResponse({"html": html})
    