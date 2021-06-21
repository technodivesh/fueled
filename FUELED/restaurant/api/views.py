from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from restaurant.models import Restaurant, Review, Comment
from .serializers import RestaurantSerializer


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
		print("request.data--", request.data)
		print("serializer--", serializer)
		if serializer.is_valid():
			serializer.save()
			return Response({'message':'Restaurant created'}, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


		pass

	# def update(self,request,pk=None):
	# 	pass

	# def destroy(elf,request,pk=None):
	# 	pass