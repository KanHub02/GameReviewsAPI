from rest_framework import serializers
from users.models import UserContacts


class UnFollowByCurrentUserSerializer(serializers.ModelSerializer):
    user_from = serializers.CurrentUserDefault
    user_to = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserContacts
        fields = ["user_to"]


class FollowerSystemSerializer(serializers.ModelSerializer):
    user_from = serializers.CurrentUserDefault
    user_to = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserContacts
        fields = ["user_to"]


class GetAllFollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts
        fields = ["user_to"]


class GetAllFollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContacts
        fields = ["user_from"]
