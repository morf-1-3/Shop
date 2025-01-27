from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ShopInfo)
class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ["shop_name","email","phone","adress",
                    "social_media","work_span","logo","short_descriprion"
                    ]
    
    def short_descriprion(self,obj):
        rez = obj.descriptions[:100] + (" .." if len(obj.descriptions)>100 else "")
        return rez 