from rest_framework import serializers
from .models import User, UserLibrary, UserContacts
from .services import LastActivity
import datetime

get_correct_str_time_ru = LastActivity.get_correct_str_time_ru


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=40, min_length=8)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=40)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    image = serializers.ImageField()
    telegram_account = serializers.CharField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=80)
    status = serializers.CharField(max_length=100)
    get_follows_count = serializers.SerializerMethodField(
        method_name="get_follows_count", read_only=True
    )
    get_followers_count = serializers.SerializerMethodField(
        method_name="get_followers_count", read_only=True
    )

    def get_follows_count(self, obj):
        return UserContacts.objects.filter(user_to=obj).count()

    def get_followers_count(self, obj):
        return UserContacts.objects.filter(user_from=obj).count()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "image",
            "telegram_account",
            "first_name",
            "last_name",
            "get_follows_count",
            "get_followers_count",
            "status",
        ]
