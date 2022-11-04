from django.urls import path, include
from .views import GameListView


urlpatterns = [path("games", GameListView.as_view())]
