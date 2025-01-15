from django.urls import path
from .views import *
urlpatterns = [
    path('<str:category>/',show_category),
    path('<str:category>/<int:item_id>',show_item),
    path("",show_items)
]