from django.urls import path
from .models import *
from .views import *
urlpatterns = [
    path("",main),
    path('get_cart/',get_cart),
    path('get_cart/<int:product_id>/',add_to_cart),
    path('plus_count_product/<int:product_id>/',plus_count_cart),
    path('minus_count_product/<int:product_id>/',minus_count_cart),
    path('remove_product/<int:product_id>/',remove_count_cart)
]