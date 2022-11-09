from rest_framework import serializers
from ..models import Rating, Game, Publisher
from users.models import Ip


class GameSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()

    class Meta:
        model = Game
        fields = ("id title image description publisher").split()


class GameDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    #views_count = serializers.SerializerMethodField(method_name="views_count", read_only=True)
    

    class Meta:
        model = Game
        fields = ("id title image description publisher tag rating created_at views").split()
    

    def views_count(self, instance):
        return Game.objects.filter(views=instance).count()


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
