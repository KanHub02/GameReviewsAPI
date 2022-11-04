from django.shortcuts import render
from rest_framework import generics, status, response
from media_api.serializers.serializers import GameSerializer, PublisherSerializer
from .models import Game, Publisher, Tag, Rating


class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = []
    queryset = Game.objects.all()
