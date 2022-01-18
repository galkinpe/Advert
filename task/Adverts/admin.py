from django.contrib import admin
from .models import City, Category, Advert 


@admin.register(Category)
@admin.register(City)
@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass
    
    
    
    
    
    #list_display = ('id', 'title', 'views')
    #list_display_links = ('id', 'title')
    #search_fields = ('title', 'description')







#class AdvertAdmin(admin.ModelAdmin):
#list_display = ( 'id', 'title', 'views')
#@admin.register(Category)
#@admin.register(City)
#@admin.register(Advert, AdvertAdmin)
