from rest_framework import serializers
from .models import Restaurant, Review


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        # fields = ['name', 'desc', 'locality', 'city', 'user']
        fields = '__all__'
