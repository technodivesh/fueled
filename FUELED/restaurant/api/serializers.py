from rest_framework import serializers
from restaurant.models import Restaurant, Review


# class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant

        fields = '__all__'
        # fields = ['name', 'desc', 'locality', 'city', 'added_by']
