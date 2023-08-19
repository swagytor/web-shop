import datetime
from django.utils import timezone
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='категория')
    category_description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название товара')
    product_description = models.TextField(verbose_name='описание', **NULLABLE)
    product_image = models.ImageField(verbose_name='изображение', upload_to='product/', **NULLABLE)
    product_category = models.ForeignKey(Category, to_field='id', default=None, on_delete=models.deletion.CASCADE, verbose_name='категория')
    product_price = models.FloatField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(verbose_name='дата создания', default=timezone.now)
    date_of_last_change = models.DateField(verbose_name='дата последнего изменения', default=timezone.now)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
