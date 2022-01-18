from django.contrib import admin

from .models import City, Category, Advert 

class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views')
    #list_display_links = ('id', 'title')
    #search_fields = ('title', 'description')


#class AdvertAdmin(admin.ModelAdmin):
    #list_display = ( 'id', 'title', 'views')
admin.site.register(Advert)
admin.site.register(Category)
admin.site.register(City)



    