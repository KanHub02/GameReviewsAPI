from django.urls import path, include
from .views import UserRegisterView, LoginView, ProfileUpdateView, ProfileViewSet
from users.contacts.contact_urls import urlpatterns as contact_urlpatterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"profile", ProfileViewSet, "get_profile_api")


urlpatterns = [
    path("sign-up/", UserRegisterView.as_view(), name="sign-in_api"),
    path("sign-in/", LoginView.as_view(), name="sign-in_api"),
    path("profile-update/", ProfileUpdateView.as_view()),
    path("", include(router.urls))
]

urlpatterns += contact_urlpatterns
