from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from fldUser.models import User
from .serializers import UserSerializer, SignUpSerializer,LoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
import jwt, datetime
from rest_framework_simplejwt.authentication import JWTAuthentication


# from rest_framework.mixins import CreateModelMixin


class SignUpViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)

    def create(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ViewSet):

    permission_classes = (AllowAny,)
    # authentication_classes = (JWTAuthentication,)

    def create(self, request):

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class LogOutViewSet(viewsets.ViewSet):

    def create(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout Successfully'
        }
        return response

class UserViewSet(viewsets.ViewSet):

    # permission_classes = (IsAuthenticated,)

    # def list(self,request):

    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)


    def list(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            # payload = jwt.decode(token, 'secret', algorithm=['HS256'])
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        print("payload--", payload)
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        # serializer = LoginSerializer(user)
        return Response(serializer.data)

# class UserViewSet(viewsets.ViewSet):

#     permission_classes = (IsAuthenticated,)

#     def list(self,request):

#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None):

#         user = User.objects.get(id=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     # def create(self,request):
#     #     serializer = UserSerializer(data=request.data)
#     #     # print("request.data--", request.data)
#     #     # print("serializer--", serializer)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request,pk=None):
#         user = User.objects.get(id=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'User Updated'}, status=status.HTTP_202_ACCEPTED)

#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#     # def partial_update(self, request, pk=None):
#     #     user = User.objects.get(id=pk)
#     #     serializer = UserSerializer(user, data=request.data,partial=True)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({'message':'User Updated'}, status=status.HTTP_202_ACCEPTED)

#     #     return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#     def destroy(self,request,pk=None):
#         user = User.objects.get(id=pk)
#         user.delete()
#         return Response({'message':'User Deleted'}, status=status.HTTP_202_ACCEPTED)

# Ref from
# https://www.django-rest-framework.org/api-guide/viewsets/