from django.contrib import admin
#from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
from .models import Restaurant, Review, Comment,ThumbDown,Visited

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(ThumbDown)
admin.site.register(Visited)
