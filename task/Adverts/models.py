from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name =  models.CharField(max_length=200, verbose_name = 'Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
       

class City(models.Model):
    name =  models.CharField(max_length=200,)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class Advert(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    city = models.ForeignKey('City', on_delete=models.PROTECT,verbose_name='Город')
    category = models.ManyToManyField('Category',verbose_name='Категория')
    views = models.IntegerField (default=0, verbose_name='Просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Обновлено') 
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        