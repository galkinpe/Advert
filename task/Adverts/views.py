from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Advert, Category, City
from django.shortcuts import redirect
from django.views.generic import View


class AdvertList(ListView):
    model = Advert
    template_name = 'adverts/base.html'
    queryset = model.objects.all()

class AdvertDetail(DetailView):
    model=Advert
    template_name = 'adverts/advert_list.html'
    queryset = model.objects.all()

    def get_queryset(self):
       queryset = super().get_queryset()
       return queryset.filter(author=self.request.user)