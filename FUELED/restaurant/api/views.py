from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from restaurant.models import Restaurant, Review, Comment
# from django.contrib.auth.models import User
from .serializers import RestaurantSerializer
from .serializers import ReviewSerializer
from .serializers import CommentSerializer


class RestaurantViewSet(viewsets.ViewSet):

    def list(self,request):

        restaurants = Restaurant.objects.all()
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

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


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

# Ref from
# https://www.django-rest-framework.org/api-guide/viewsets/