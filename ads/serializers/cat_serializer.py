from rest_framework import serializers

from ads.models.cat_model import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"]


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"]
