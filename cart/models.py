from django.db import models
from catalog.models import Product
# from users.models import User
from django.contrib.auth.models import User
from django.http import HttpRequest,HttpResponse
import hashlib
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Користувач",related_name="cart", null=True, blank=True)
    cart_id = models.CharField(max_length=255,blank=True,null=True)

    @classmethod
    def get_cart(cls,request:HttpRequest, response:HttpResponse=None):
        # request = response.request
        if request.user.is_authenticated:
            cart_obj = cls.objects.filter(user = request.user)
            if cart_obj:
                cart_obj = cls.objects.get(user=request.user)
                # return (response,cart_obj)
            else:
                cart_obj = cls.objects.create(user=request.user)
                # return (response,cart_obj)
        else:
            cart_id = request.COOKIES.get('cart_id')
            if cart_id:                
                cart_obj = cls.objects.filter(cart_id = cart_id)
                if cart_obj:
                    
                    cart_obj = cls.objects.get(cart_id = cart_id)
                    
                if cart_obj and response:
                    return (response,cart_obj)
                if cart_obj:
                    
                    return cart_obj
            #     else:
            #         cart_obj = cls.objects.create()
            #         cart_obj.cart_id = hashlib.sha256(str(cart_obj.id).encode()).hexdigest()
            #         cart_obj.save()
            #         response.set_cookie('cart_id', cart_obj.cart_id)
            #         return (response,cart_obj)

                

            else:
            
                cart_obj = cls.objects.create()
                cart_obj.cart_id = hashlib.sha256(str(cart_obj.id).encode()).hexdigest()
                cart_obj.save()
                # if(not response):
                #     return(cart_obj,)
                # print(response)
                # response = HttpResponse()
                if response:
                    response.set_cookie('cart_id', cart_obj.cart_id)
                
        if response:
            return (response,cart_obj)
        else:
            return cart_obj

    class Meta:
        verbose_name = "Кошик"
        verbose_name_plural = "Кошик"

    def __str__(self):
        if (self.user):
            return f"Кошик користувача {self.user.get_full_name()}"
        else:
            return f"Кошик не авторизованого користувача"

class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="products",verbose_name="Кошик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Продукти")
    count = models.PositiveIntegerField(verbose_name="Кількість", default=1)

    class Meta:
        verbose_name = "Продукт в кошику"
        verbose_name_plural = "Продукти в кошику"

    def __str__(self):
        return f"Продукти в {self.cart.user}"
