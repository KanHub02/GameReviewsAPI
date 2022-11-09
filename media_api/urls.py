from django.urls import path, include
from .views import GameListView, MobaTagListView, GameDetailView


urlpatterns = [
    path("games/", GameListView.as_view()),
    path("games/<pk>/", GameDetailView.as_view()),
    path("moba-games/", MobaTagListView.as_view()),
]
