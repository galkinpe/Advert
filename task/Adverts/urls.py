from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *


urlpatterns = [
     path('', views.AdvertList.as_view(), name='adverts'),
]
