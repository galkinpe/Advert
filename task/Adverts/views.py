from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    advert = Advert.object.all()
    context = {
        
    }


