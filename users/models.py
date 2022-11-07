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
    comment = models.TextField(
        related_name="current_user_review", null=True, blank=True
    )

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
                check=~models.Q(
                    user_from=models.F("user_to")
                ),  # Prohibits subscribing to yourself
                name="User cant follow to self",
            )
        ]


# Create your models here.
