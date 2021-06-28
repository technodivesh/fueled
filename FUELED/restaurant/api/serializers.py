from rest_framework import serializers
from restaurant.models import Restaurant, Review, Comment
# from django.contrib.auth.models import User


# class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
class RestaurantSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Restaurant

        # fields = '__all__'
        fields = ['name', 'desc', 'locality', 'city', 'added_by','reviews']


class ReviewSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    class Meta:
        model = Review

        fields = '__all__'
        # fields = ['name', 'desc', 'locality', 'city', 'added_by']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = '__all__'
        # fields = ['name', 'desc', 'locality', 'city', 'added_by']

