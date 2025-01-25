from django.db import models
from django.contrib.auth.models import User
from orders.models import Order
# Create your models here.

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефону")
    birth_day = models.DateField(verbose_name="Дата народження",blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", verbose_name="Користувач")


class Receiver(models.Model):
    first_name = models.CharField(max_length=255,verbose_name="Ім'я отримувача")
    last_name = models.CharField(max_length=255, verbose_name="Фамілія отримувача")
    phone_number = models.CharField(max_length=15,verbose_name="Номер телефону отримувача")
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="receiver")
    ref_warehouse = models.CharField(max_length=120,verbose_name="Відділення почти",default="Подзвонити для уточнення")
    class Meta:
        verbose_name = "Отримувач"
        verbose_name_plural = "Отримувачі"
    
    def __str__(self):
        return f"Отримувач {self.first_name} {self.last_name}"