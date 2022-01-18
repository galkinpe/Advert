from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert


def index(request):
    adverts = Advert.objects.all()
    context = {'adverts': adverts, 
               'title': 'Список новостей'
    }
    return render(request,'adverts/index.html',context) 





