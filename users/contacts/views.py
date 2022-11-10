from users.contacts.serializers import (
    FollowerSystemSerializer,
    UnFollowByCurrentUserSerializer,
    GetAllFollowersSerializer,
    GetAllFollowsSerializer,
    
)

from rest_framework import generics
from rest_framework import views
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import User, UserContacts


class UnFollowByView(generics.DestroyAPIView):

    queryset = UserContacts.objects.all()
    serializer_class = UnFollowByCurrentUserSerializer
    authentication_classes = [JWTAuthentication]

    def destroy(self, request, pk):
        user = UserContacts.objects.get(user_to_id=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_destroy(user)
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data="Current user unfollow succesfully",
            )


class GetToFollowView(views.APIView):
    serializer_class = FollowerSystemSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user_from=request.user, user_to=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllFollows(generics.ListAPIView):
    serializer_class = GetAllFollowsSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    # pagination_class = FollowersPagination

    # pagination_classes = CommentPagination

    def get(self, request, pk):
        post = get_object_or_404(User, pk=pk)
        follows_data = self.serializer_class(
            post.from_set, many=True, context={"request": request}
        ).data

        return Response(data=follows_data)


class GetAllFollowers(generics.ListAPIView):
    serializer_class = GetAllFollowersSerializer
    [
        IsAuthenticated,
    ]
    # pagination_class = FollowersPagination

    def get(self, request, pk):
        post = get_object_or_404(User, pk=pk)
        followers_data = self.serializer_class(
            post.to_set, many=True, context={"request": request}
        ).data

        return Response(data=followers_data)
