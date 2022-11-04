from distutils.command.upload import upload
from email.policy import default
from django.db import models
from managers.game_manager import GameQuerySet, GameManager
from django.db.models import Avg
from .settings import star_choices


class Rating(models.Model):
    user = models.ManyToManyField("User", unique=True)
    stars = models.Choices(choices=star_choices, default=0.0)


    def __str__(self):
        return self.id


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзыв"
        


class Publisher(models.Model):
    
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()

    @property
    def get_avg_rating(self):
        return self.objects.annotate(Avg("rating"))


class Tag(models.Model):
    name = models.CharField(max_length=50)

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
    rating = models.PositiveIntegerField()




    objects = GameManager()
    tag_manager = GameManager()

    def __str__(self):
        return self.title


    @property
    def get_avg_rating(self):
        return self.objects.annotate(Avg("rating"))


    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = "Игра"


# Create your models here.
