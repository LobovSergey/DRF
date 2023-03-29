from rest_framework import serializers

from ads.models.ads_model import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Announcement
        fields = "__all__"


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Announcement
        fields = "__all__"


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ["is_published"]


class AnnouncementDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement


class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ["is_published"]
