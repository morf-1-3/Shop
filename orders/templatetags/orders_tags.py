from django import template
from ..services.nova_posta import *

register = template.Library()

@register.inclusion_tag("orders/dropdown_cities.html")
def show_main_cities(query_name=None):
    if query_name:
        settlements = get_settlements(query_name)
        return {"main_sities" : settlements}
    else:
        return {"main_sities": main_sities}

# @register.inclusion_tag("orders/dropdown_find_settlements.html")
# def show_finded_settlements():
#     finded_settlements = 
#     return {"finded_settlements": finded_settlements}