from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.shortcuts import render
from .models import Advert, Category, City
from django.shortcuts import redirect
from django.views.generic import View


class AdvertList(ListView):
    model = Advert
    template_name = 'adverts/adverts_list.html'
    queryset = model.objects.all()







