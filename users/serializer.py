from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=40, min_length=8)
    password2 = serializers.CharField(max_length=40, min_length=8)

    def validate(self, attrs):
        if attrs["password2"] != attrs["password"]:
            raise serializers.ValidationError("Passwords didn't match")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

    class Meta:
        models = User
        fields = ["email", "username", "password", "password2"]
