from django.db import models
from catalog.models import *

# Create your models here.

class ShopInfo(models.Model):
    shop_name = models.CharField(max_length=100, verbose_name="Назва магазину")
    email = models.EmailField(max_length=100,verbose_name="Емейл")
    phone = models.CharField(max_length=14, verbose_name="Номер телефону")
    adress = models.CharField(max_length=150, verbose_name="Адресса")
    social_media = models.JSONField(verbose_name="Соціальні мережі")
    work_span = models.JSONField(verbose_name="Графік роботи")
    logo = models.ForeignKey(Image,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Лого")
    descriptions = models.TextField(verbose_name="Опис магазину")

    class Meta:
        verbose_name = "Інформація про магазин"
        verbose_name_plural = "Інформація про магазин"

    def __str__(self):
        return f"Інформація про {self.shop_name}"
    

