from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from restaurant.models import Restaurant, Review, Comment
# from django.contrib.auth.models import User
from .serializers import RestaurantSerializer
# from .serializers import UserSerializer


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

    def destroy(elf,request,pk=None):
        resto = Restaurant.objects.get(id=pk)
        resto.delete()
        return Response({'message':'Restaurant Deleted'}, status=status.HTTP_202_ACCEPTED)

# Ref from
# https://www.django-rest-framework.org/api-guide/viewsets/