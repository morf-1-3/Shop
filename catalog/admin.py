from django.contrib import admin
from .models import Category, Product, Image
from django.utils.html import mark_safe
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["alt_text", 'get_image']

    def get_image(self,obj):
        if obj.image:
            return mark_safe(f'''<img src="{obj.image.url}" alt="{obj.alt_text}" 
                             width="100" height = "100" >''')
        return "no image"
    get_image.short_discription = "Фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","description","parent_category", "image_get"]
   
    def image_get(self,obj):
        if obj.image and obj.image.image:
            return mark_safe(f'''<img src="{obj.image.image.url}" alt="{obj.image.alt_text}" 
                             width="100" height = "100" >''')
        return "no image"
    
    image_get.short_description = "Фото"

      

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price","category", "stock",'get_images']
    

    def get_images(self,obj):
        if obj.images:
            images = obj.images.all()
            return mark_safe("".join([f'''<image src="{image.image.url}" 
                                      alt="{image.alt_text}" width="100" height = "100" >'''for image in images[:3]]))
    get_images.short_description ="Фотографії"                                  