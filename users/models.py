from django.db import models
from .managers import UserBaseManager


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    image = models.ImageField(upload_to="media", default="media/default/avatar.png")

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    objects = UserBaseManager()

    USERNAME_FIELD = "username"
    USERNAME_FIELD = ["email"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ManyToManyField("media_api.Game")


# Create your models here.
