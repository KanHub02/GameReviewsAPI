from rest_framework.generics import CreateAPIView
from .serializer import UserRegisterSerializer
from rest_framework import status, views
from .models import User
from .permissions import IsAnonymous



class UserRegisterView(CreateAPIView):
    queryset = User
    serializer_class = [UserRegisterSerializer]
    permission_classes = [IsAnonymous]
# Create your views here.
