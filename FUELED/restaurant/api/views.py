from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from restaurant.models import Restaurant, Review, Comment
from restaurant.models import ThumbDown, Visited
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .serializers import RestaurantSerializer
from .serializers import ReviewSerializer
from .serializers import CommentSerializer
from .serializers import ThumbDownSerializer
from .serializers import VisitedSerializer
import json

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly 
from rest_framework_simplejwt.tokens import AccessToken

class RestaurantViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self,request):

        """
        If GET request will be send with param all=true 
        all records will be returned without filtering of thumbsdowm records
        """

        # token_str = request.META.get('HTTP_AUTHORIZATION')
        user_id = request.user.id
        print("user_id---",user_id)

        if request.GET.get('all') == 'true':
            restaurants = Restaurant.objects.all()
        else:
            # TODO: Get user_id from token
            inner_qs = ThumbDown.objects.filter(user=user_id).values_list('restaurant',flat=True).distinct()
            restaurants = Restaurant.objects.exclude(id__in=inner_qs)

        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        restaurants = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(restaurants)
        return Response(serializer.data)

    def create(self,request):
        serializer = RestaurantSerializer(data=request.data)
        # print("request.data--", request.data)
        # print("serializer--", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Restaurant created'}, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


    def update(self,request,pk=None):
        resto = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(resto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Restaurant Updated'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        resto = Restaurant.objects.get(id=pk)
        serializer = RestaurantSerializer(resto, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Restaurant Updated'}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request,pk=None):
        resto = Restaurant.objects.get(id=pk)
        resto.delete()
        return Response({'message':'Restaurant Deleted'}, status=status.HTTP_202_ACCEPTED)


class ReviewViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly ,)

    def list(self,request):

        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def create(self,request):
        serializer = ReviewSerializer(data=request.data)
        # print("request.data--", request.data)
        # print("serializer--", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Review created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


    def update(self,request,pk=None):
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Review Updated'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Review Updated'}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request,pk=None):
        review = Review.objects.get(id=pk)
        review.delete()
        return Response({'message':'Review Deleted'}, status=status.HTTP_202_ACCEPTED)


class CommentViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly ,)

    def list(self,request):

        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def create(self,request):
        serializer = CommentSerializer(data=request.data)
        # print("request.data--", request.data)
        # print("serializer--", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Comment created'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


    def update(self,request,pk=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Comment Updated'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Comment Updated'}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request,pk=None):
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return Response({'message':'Comment Deleted'}, status=status.HTTP_202_ACCEPTED)


class ThumbDownViewSet(viewsets.ViewSet):
    
    """
    get:
    A description of the get method on the custom action.

    post:
    A description of the post method on the custom action.
    """ 
    permission_classes = (IsAuthenticated,)
    def list(self,request):

        user_id = request.GET.get('user_id', None)
        thumbdown = ThumbDown.objects.filter(user=user_id).values_list('restaurant',flat=True).distinct()
        # serializer = ThumbDownSerializer(thumbdown, many=True)
        # print("user_id--",user_id)
        # return Response(serializer.data)
        return Response(thumbdown)

    # def retrieve(self,request,pk=None):

    #     # thumbdown = ThumbDown.objects.get(user=pk)
    #     user_id = self.request.GET.get('user', None)
    #     thumbdown = ThumbDown.objects.filter(user=user_id)
    #     serializer = ThumbDownSerializer(thumbdown)
    #     return Response(serializer.data)

    def create(self,request):

        """
        param1 -- A first parameter
        param2 -- A second parameter
        """ 
        print("request---",request.user)
        ############################
        # from rest_framework_simplejwt.backends import TokenBackend
        # token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        # data = {'token': token}
        #    try:
        #       valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        #       user = valid_data['user']
        #       request.user = user
        #    except ValidationError as v:
        #       print("validation error", v)
      ###############################################
        serializer = ThumbDownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'ThumbDown Marked'}, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request,pk=None):
        thumbdown = ThumbDown.objects.get(id=pk)
        thumbdown.delete()
        return Response({'message':'ThumbDown Removed'}, status=status.HTTP_202_ACCEPTED)


class VisitedViewSet(viewsets.ViewSet):

    # permission_classes = (IsAuthenticatedOrReadOnly ,)
    def list(self,request):

        visited = Visited.objects.all()
        # user_id = self.request.GET.get('user', None)
        # visited = Visited.objects.filter(user=user_id)
        serializer = VisitedSerializer(visited, many=True)
        return Response(serializer.data)

    # def retrieve(self,request,pk=None):

    #     visited = Visited.objects.filter(user=pk)
    #     serializer = VisitedSerializer(visited)
    #     return Response(serializer.data)

    def create(self,request):
        serializer = VisitedSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Visited Marked'}, status=status.HTTP_201_CREATED)

        # return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request,pk=None):
        visited = Visited.objects.get(id=pk)
        visited.delete()
        return Response({'message':'Visited Removed'}, status=status.HTTP_202_ACCEPTED)
# Ref from
# https://www.django-rest-framework.org/api-guide/viewsets/