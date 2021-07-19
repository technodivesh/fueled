from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from fldUser.models import User
from .serializers import UserSerializer, RegisterSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BasicAuthentication
import jwt, datetime
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions

# from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.schemas import ManualSchema, AutoSchema
import coreapi,coreschema

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False
#############################

class RegisterViewSet(viewsets.ViewSet):
    """
    create:
    Anyone can create a account.

    """

    permission_classes = (AllowAny,)



    # schema = ManualSchema(fields=[
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "username",
            description="TEst",
            required=True,
            location="path",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "email",
            required=True,
            location="path",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "password",
            required=True,
            location="path",
            schema=coreschema.String()
        ),
    ])


    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        print("request.data--", request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):

    """
    list:
    Only Admin user can get list of users.

    retrieve:
    Any authenticated user can get its own details.
    """
    serializer_class = UserSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['update', 'partial_update', 'destroy', 'retrieve'],
        IsAdminUser: ['list']
    }

    def list(self,request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):

        # print(request.user.username)
        # print(request.user.id)
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

