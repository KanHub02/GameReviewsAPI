from django.urls import path, include
from .views import GameListView, MobaTagListView


urlpatterns = [
    path("games", GameListView.as_view()),
    path("moba-games/", MobaTagListView.as_view()),
]
