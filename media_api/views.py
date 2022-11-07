from django.shortcuts import render
from rest_framework import generics, status, response, views
from media_api.serializers.serializers import GameSerializer, PublisherSerializer
from .models import Game, Publisher, Tag, Rating


class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = []
    queryset = Game.objects.all()


class MobaTagListView(views.APIView):
    serializer_class = GameSerializer

    def get(self, request):
        instance = Game.objects.filter(tag__name="moba")
        data = self.serializer_class(instance, many=True).data
        return response.Response(data=data, status=status.HTTP_200_OK)
