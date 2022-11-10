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


class ProfileUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, read_only=True)
    email = serializers.EmailField(read_only=True)
    image = serializers.ImageField()
    telegram_account = serializers.CharField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=80)
    status = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "image",
            "telegram_account",
            "first_name",
            "last_name",
            "status",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    contacts_count = serializers.SerializerMethodField(read_only=True, method_name="contacts_count")
    class Meta:
        model = User
        exclude = ["is_superuser", "is_staff", "is_active", "is_private", "password"]

    
    def contacts_count(self, instance):
        return UserContacts.objects.filter(to_set=instance).count()