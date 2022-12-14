from django.db import models
from .managers import UserBaseManager
from .settings import telegram_validator, status_choices
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class Ip(models.Model):
    ip = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.ip

    class Meta:
        verbose_name = "Айпи адрес просмотра"
        verbose_name_plural = "Айпи адреса просмотров"


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="media", default="media/default/avatar.png")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    # status = models.CharField(choices=[status_choices], max_length=100, null=True, blank=True)
    # Profile fields
    telegram_account = models.CharField(
        validators=[telegram_validator], null=True, blank=True, max_length=100
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)

    objects = UserBaseManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    views = models.ManyToManyField("self")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ManyToManyField("media_api.Game")
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} библиотека"

    class Meta:
        verbose_name = "Библиотека игр"
        verbose_name_plural = "Библиотека игр"


class UserContacts(models.Model):
    user_to = models.ForeignKey(
        User,
        related_name="to_set",
        on_delete=models.CASCADE,
        verbose_name="To",
    )
    user_from = models.ForeignKey(
        User,
        related_name="from_set",
        on_delete=models.CASCADE,
        verbose_name="By",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Created"
    )

    def __str__(self) -> str:
        return f"{self.user_from} contact with {self.user_to}"

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user_from=models.F("user_to")),
                name="User cant follow to self",
            )
        ]


class Team(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/team/upload_to/")
    captain = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="team_captain"
    )
    members = models.ManyToManyField(User, related_name="team_member")
    rating = models.IntegerField()

    def __str__(self):
        return f"Капитан-{self.captain} Команда-{self.title}"

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


# Create your models here.
