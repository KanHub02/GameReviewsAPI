from distutils.command.upload import upload
from email.policy import default
from django.db import models
from media_api.managers.game_manager import GameQuerySet, GameManager
from django.db.models import Avg
from .settings import star_choices


class Rating(models.Model):
    # user = models.ManyToManyField("User", unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"


class Publisher(models.Model):

    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=star_choices, default=0.0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    @property
    def get_avg_rating(self):
        return self.objects.annotate(Avg("rating"))

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категория"


class Game(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="media")
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, blank=True, null=True)
    born_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # objects = GameQuerySet()
    # tag_manager = GameManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = "Игра"


# Create your models here.
