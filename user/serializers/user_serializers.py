from rest_framework import serializers

from user.models.user_model import User


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = User
        exclude = ['password']


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'location']


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'location']
