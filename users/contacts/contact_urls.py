from django.urls import path, include
import views


urlpatterns = [
    path("user/<pk>/follow/", views.GetToFollowView.as_view(), name="to_follow_api"),
    path(
        "user/<pk>/followers/",
        views.GetAllFollowers.as_view(),
        name="user_followers_api",
    ),
    path("user/<pk>/follows/", views.GetAllFollows.as_view(), name="user_follows_api"),
    path("user/<pk>/unfollow/", views.UnFollowByView.as_view(), name="to_unfollow_api"),
]
