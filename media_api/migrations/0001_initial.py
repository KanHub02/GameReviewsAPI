# Generated by Django 4.1.2 on 2022-11-04 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("rating", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stars",
                    models.IntegerField(
                        choices=[
                            (1, "*"),
                            (2, "**"),
                            (3, "***"),
                            (4, "****"),
                            (5, "*****"),
                        ],
                        default=0.0,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзыв",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Категории",
                "verbose_name_plural": "Категория",
            },
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="media_api.publisher",
                    ),
                ),
                (
                    "rating",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="media_api.rating",
                    ),
                ),
                ("tag", models.ManyToManyField(null=True, to="media_api.tag")),
            ],
            options={
                "verbose_name": "Игры",
                "verbose_name_plural": "Игра",
            },
        ),
    ]