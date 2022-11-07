from django.urls import path
from .views import UserRegisterView


url_patterns = [path("sign-up/", UserRegisterView.as_view(), name="sign-in_api")]
