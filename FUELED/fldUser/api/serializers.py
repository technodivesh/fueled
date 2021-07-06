from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from fldUser.models import User
from django.contrib.auth import authenticate

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        # fields = '__all__'
        fields = ['id','username', 'email']

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance