from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, response, views
from media_api.serializers.serializers import GameSerializer, PublisherSerializer
from .models import Game, Publisher, Tag, Rating
from users.models import Ip
from users.services import Viewer


class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = []
    queryset = Game.objects.all()


class GameDetailView(views.APIView):
    serializer_class = GameSerializer

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Game, pk=pk)
        ip = Viewer.get_client_ip(request)
        serializer = self.serializer_class(post, many=False).data

        if Ip.objects.filter(ip=ip).exists():
            post.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            post.views.add(Ip.objects.get(ip=ip))

        return response.Response(data=serializer, status=status.HTTP_200_OK)



class MobaTagListView(views.APIView):
    serializer_class = GameSerializer

    def get(self, request):
        instance = Game.objects.filter(tag__name="moba")
        data = self.serializer_class(instance, many=True).data
        return response.Response(data=data, status=status.HTTP_200_OK)
