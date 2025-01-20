from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефону")
    birth_day = models.DateField(verbose_name="Дата народження",blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile", verbose_name="Користувач")

