from rest_framework import serializers
from restaurant.models import Restaurant, Review, Comment
from restaurant.models import ThumbDown, Visited

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = '__all__'
        # depth = 1

class ReviewSerializer(serializers.ModelSerializer):
    # comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Review

        fields = '__all__'
        # depth = 1
        
# class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
class RestaurantSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = Restaurant

        # fields = '__all__'
        fields = ['name', 'desc', 'locality', 'city', 'added_by','reviews']
        # depth = 1




class ThumbDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbDown

        fields = '__all__'

class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visited

        fields = '__all__'

