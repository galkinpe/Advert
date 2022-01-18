from django.conf import settings
from django.db import models


class Category(models.Model):
    name =  models.CharField(max_length=200,)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class City(models.Model):
    name =  models.CharField(max_length=200,)


    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Advert(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание',)
    city = models.ForeignKey('City', on_delete=models.PROTECT,)
    category = models.ForeignKey('Category', on_delete=models.PROTECT )
    views = models.IntegerField (default = 0)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        