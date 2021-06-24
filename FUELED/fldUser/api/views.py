from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):

    def list(self,request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self,request):
        serializer = UserSerializer(data=request.data)
        # print("request.data--", request.data)
        # print("serializer--", serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Updated'}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Updated'}, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(elf,request,pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response({'message':'User Deleted'}, status=status.HTTP_202_ACCEPTED)

# Ref from
# https://www.django-rest-framework.org/api-guide/viewsets/