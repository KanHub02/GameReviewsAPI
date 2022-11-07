from rest_framework import serializers
from ..models import Rating, Game, Publisher


class GameSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = ("id title image description publisher tag rating created_at").split()


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
