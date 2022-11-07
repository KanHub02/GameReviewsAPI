from rest_framework import serializers
from .models import User
from .services import LastActivity
import datetime

get_correct_str_time_ru = LastActivity.get_correct_str_time_ru





class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=40, min_length=8)
    password2 = serializers.CharField(max_length=40, min_length=8)
    get_last_activity = serializers.SerializerMethodField(read_only=True)


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


    def get_last_activity(self, instance):
        try:
            now = datetime.utcnow()
            last_seen = now - instance.last_active
            if 30 >= last_seen.days > 0:
                a = get_correct_str_time_ru(last_seen.days, 'd')
            elif last_seen.days > 30:
                return "Был(а) давно"
            else:
                if last_seen.seconds // 3600 > 0:
                    a = get_correct_str_time_ru(last_seen.seconds // 3600, 'h')
                elif last_seen.seconds // 60 % 60:
                    a = get_correct_str_time_ru(last_seen.seconds // 60 % 60, 'm')
                else:
                    a = get_correct_str_time_ru(last_seen.seconds % 60, 's')
            return a
        except:
            return "Был(а) давно"
