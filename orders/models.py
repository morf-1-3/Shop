from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
# Create your models here.
statuses = {
    "1": "InProces",
    "2": "Ready"
}

class OrderStatus(models.TextChoices):
    IN_PROCESS = "1", "In Process"
    READY = "2", "Ready"

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Користувач", related_name="orders")
    customer = models.CharField(max_length=255, null=True,blank=True, verbose_name="Користувач")
    create_at = models.DateTimeField(verbose_name="Створено в:",auto_now_add=True)
    status = models.CharField(max_length=2,choices=OrderStatus.choices,default=OrderStatus.IN_PROCESS,verbose_name="Статус")

    def __str__(self):
        return f"Замовлення {self.id} - {self.get_status_display()}"

    def get_total_price(self) ->float:
        products = self.products.all()
        total_price:float = 0
        for product in products:
            total_price += product.get_price


    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

class ProductInOrder(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,verbose_name="Продукт",null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, verbose_name="Замовлення",null=True, related_name="products")
    count = models.PositiveIntegerField(verbose_name="Кількість",default=1)

    def __str__(self):
        return f"{self.product.name} в кількості {self.count}"
    
    def get_price(self) -> float:
        return self.count * (self.product.price if self.product.price else 0)


    class Meta:
        verbose_name = "Продукт в кошику"
        verbose_name_plural = "Продукти в кошику"


