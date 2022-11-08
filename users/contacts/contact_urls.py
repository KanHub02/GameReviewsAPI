from django.urls import path, include
from .views import GetAllFollowers, GetAllFollows, GetToFollowView, UnFollowByView


urlpatterns = [
    path("user/<pk>/follow/", GetToFollowView.as_view(), name="to_follow_api"),
    path(
        "user/<pk>/followers/",
        GetAllFollowers.as_view(),
        name="user_followers_api",
    ),
    path("user/<pk>/follows/", GetAllFollows.as_view(), name="user_follows_api"),
    path("user/<pk>/unfollow/", UnFollowByView.as_view(), name="to_unfollow_api"),
]
