from django.contrib import admin
from .models import Advert,City,Category


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

    


    
    
    
    
    
    
