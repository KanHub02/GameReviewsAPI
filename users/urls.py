from django.urls import path
from .views import UserRegisterView, LoginView
from users.contacts.contact_urls import urlpatterns as contact_urlpatterns


urlpatterns = [
    path("sign-up/", UserRegisterView.as_view(), name="sign-in_api"),
    path("sign-in/", LoginView.as_view(), name="sign-in_api"),
]

urlpatterns += contact_urlpatterns
