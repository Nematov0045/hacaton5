from django.db import models
from django.contrib import admin
# Create your models here.
class Market(models.Model):
    title = models.CharField('Название',max_length=100) 
    image = models.ImageField("Изображение", upload_to='upload/products')
    price = models.CharField("цена",max_length=20, default='', blank=True, null=True)
    description = models.CharField("описание",max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return self.title
   
class Market(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)   