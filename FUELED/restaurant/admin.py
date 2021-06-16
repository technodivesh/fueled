from django.contrib import admin

# Register your models here.
from .models import Restaurant, Review, Comment

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Comment)
