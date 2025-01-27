from django import template
from ..models import *
from django.utils.safestring import mark_safe

register = template.Library()

def get_shop_info_fiels(field:str):
    shop_info = ShopInfo.objects.first()
    return getattr(shop_info,field,None) if shop_info else None

@register.simple_tag
def show_adress():
    return  get_shop_info_fiels("adress")
            


@register.simple_tag
def show_shop_name():
    return  get_shop_info_fiels("shop_name")
            


@register.simple_tag
def show_email():
    return  get_shop_info_fiels("email")
            


@register.simple_tag
def show_phone():
    return get_shop_info_fiels("phone")
           


@register.simple_tag
def show_logo():
    return  get_shop_info_fiels("logo").image.url
          


@register.simple_tag
def show_description():
    return  mark_safe(get_shop_info_fiels("descriptions"))
            


@register.simple_tag
def show_work_span_on():
    return  get_shop_info_fiels("work_span")["weekday"]
            


@register.simple_tag
def show_work_span_of():
    return  get_shop_info_fiels("work_span")["weekend"]
            



@register.simple_tag
def show_instagram():
    return  get_shop_info_fiels("social_media")["instagram"]
            


@register.simple_tag
def show_facebook():
    return  get_shop_info_fiels("social_media")["facebook"]
            


@register.simple_tag
def show_telegram():
    return  get_shop_info_fiels("social_media")["telegram"]
            

# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_adress():
#     return {"label": "adress",
#             "value": get_shop_info_fiels("adress")
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_shop_name():
#     return {"label": "shop_name",
#             "value": get_shop_info_fiels("shop_name")
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_email():
#     return {"label": "email",
#             "value": get_shop_info_fiels("email")
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_phone():
#     return {"label": "phone",
#             "value": get_shop_info_fiels("phone")
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_logo():
#     return {"label": "logo",
#             "value": get_shop_info_fiels("logo")
#             }


# @register.simple_tag
# def show_description():
#     return  mark_safe(get_shop_info_fiels("descriptions"))
            


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_work_span_on():
#     return {"label": "work_span",
#             "value": get_shop_info_fiels("work_span")["weekday"]
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_work_span_of():
#     return {"label": "work_span",
#             "value": get_shop_info_fiels("work_span")["weekend"]
#             }



# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_instagram():
#     return {"label": "instagram",
#             "value": get_shop_info_fiels("social_media")["instagram"]
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_facebook():
#     return {"label": "facebook",
#             "value": get_shop_info_fiels("social_media")["facebook"]
#             }


# @register.inclusion_tag("shopInfo/inclusion/shopInfo.html")
# def show_telegram():
#     return {"label": "telegram",
#             "value": get_shop_info_fiels("social_media")["telegram"]
#             }




