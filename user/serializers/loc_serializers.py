from rest_framework import serializers

from user.models.user_model import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['id']


class LocationDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location


class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ['id']
