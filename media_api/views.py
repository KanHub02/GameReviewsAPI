from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, response, views
from media_api.serializers.serializers import GameSerializer, PublisherSerializer, GameDetailSerializer
from .models import Game, Publisher, Tag, Rating
from users.models import Ip
from users.services import Viewer
from .tasks import get_view


class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = []
    queryset = Game.objects.all()


class GameDetailView(views.APIView):
    serializer_class = GameDetailSerializer

    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Game, pk=pk)
        serializer = self.serializer_class(instance, many=False).data
        ip = Viewer.get_client_ip(request)
        get_view(instance, ip)

        return response.Response(data=serializer, status=status.HTTP_200_OK)


class MobaTagListView(views.APIView):
    serializer_class = GameSerializer

    def get(self, request):
        instance = Game.objects.filter(tag__name="moba")
        data = self.serializer_class(instance, many=True).data
        return response.Response(data=data, status=status.HTTP_200_OK)
