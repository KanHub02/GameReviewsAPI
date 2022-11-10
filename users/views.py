from rest_framework.generics import CreateAPIView, UpdateAPIView
from .serializer import UserRegisterSerializer, LoginSerializer, ProfileUpdateSerializer, ProfileSerializer
from rest_framework import status, views, response, viewsets
from .models import User
from .permissions import IsAnonymous, UserEquelProfile
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class =  ProfileSerializer
    authentication_classes = [JWTAuthentication]


class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [UserEquelProfile]
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()


class UserRegisterView(views.APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(
                data={
                    "status": "User register successfully",
                    "username": serializer.data["username"],
                },
                status=status.HTTP_201_CREATED,
            )


class LoginView(views.APIView):
    try:

        def post(self, request):
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]
                password = serializer.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    return response.Response(
                        data={"Error": "Username or password is wrong"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)
                data = {
                    "status": status.HTTP_200_OK,
                    "username": request.data["username"],
                    "access_token": str(access),
                    "refresh_token": str(refresh),
                }
                return response.Response(data=data, status=status.HTTP_200_OK)
            return response.Response(
                data={"Error": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception:
        raise response.Response(
            data={"Status": "Please try again"}, status=status.HTTP_400_BAD_REQUEST
        )


# Create your views here.
