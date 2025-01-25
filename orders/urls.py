from django.urls import path
from .views import *



urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('success/', make_order),
    path('nova-posta/<str:search_str>/',show_seltements,name="get_settlements"),
    path('nova-posta/',show_seltements,name="defoult_get_settlements"),
    path('nova-posta/warehouse/<str:ref>/<str:search_str>/',show_warehouses,name ="get_warehouses"),
    path('nova-posta/warehouse/<str:ref>/',show_warehouses,name="defoult_get_warehouses")
]
