from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(verbose_name="фото")
    alt_text = models.CharField(max_length=255,blank=True,null=True,verbose_name="текст")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографії"

    def __str__(self):
        if self.alt_text:
            return self.alt_text
        else:
            return "фотографія"

class Category(models.Model):
    name = models.CharField(max_length=255,verbose_name="Назва категорії")
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name="sub_categories",verbose_name="Батьківська категорія")
    description = models.TextField(verbose_name="Опис")
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, blank=True, null= True,verbose_name="фотографія")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Product(models.Model):
    name = models.CharField(max_length=255,verbose_name="Назва")
    price = models.DecimalField(max_digits=8,decimal_places=2,verbose_name="Ціна")
    images = models.ManyToManyField(Image,verbose_name='Фотографії')
    description = models.TextField(blank=True,verbose_name="Опис")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,verbose_name="Категорія",related_name="products")
    stock = models.PositiveIntegerField(default=0,verbose_name="Залишок на складі")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"