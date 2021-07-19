from rest_framework import serializers
from restaurant.models import Restaurant, Review, Comment
from restaurant.models import ThumbDown, Visited

class CommentSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_comment')
    class Meta:
        model = Comment

        fields = '__all__'
        # depth = 1

    def get_username_from_comment(self,Comment):
        try:
            return Comment.user.username
        except:
            return "Anonymous"

class ReviewSerializer(serializers.ModelSerializer):
    # comments = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    username = serializers.SerializerMethodField('get_username_from_review')
    class Meta:
        model = Review

        fields = '__all__'
        # depth = 1

    def get_username_from_review(self,Review):
        try:
            return Review.user.username 
        except:
            return "Anonymous"
        
# class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
class RestaurantSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    username = serializers.SerializerMethodField('get_username_from_restaurant')

    class Meta:
        model = Restaurant

        fields = '__all__'
        # depth = 1

    def get_username_from_restaurant(self,Restaurant):
        try:
            return Restaurant.added_by.username 
        except:
            return "Anonymous"


class ThumbDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThumbDown

        # fields = '__all__'
        fields = ['user','restaurant']

class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visited

        fields = '__all__'

