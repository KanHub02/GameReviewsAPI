# Generated by Django 4.1.2 on 2022-11-08 08:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("media_api", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=30, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "image",
                    models.ImageField(
                        default="media/default/avatar.png", upload_to="media"
                    ),
                ),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_private", models.BooleanField(default=False)),
                (
                    "telegram_account",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="The telegram username was '@XXXXXXXX'",
                                regex="^@[a-zA-Z0-9]+$",
                            )
                        ],
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=80, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.CreateModel(
            name="UserLibrary",
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
                ("comment", models.TextField(blank=True, null=True)),
                ("game", models.ManyToManyField(to="media_api.game")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Библиотека игр",
                "verbose_name_plural": "Библиотека игр",
            },
        ),
        migrations.CreateModel(
            name="UserContacts",
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Created"
                    ),
                ),
                (
                    "user_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="By",
                    ),
                ),
                (
                    "user_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="To",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
                "ordering": ("created_at",),
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                ("title", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="media/team/upload_to/")),
                ("rating", models.IntegerField()),
                (
                    "captain",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="team_captain",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("members", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name": "Команда",
                "verbose_name_plural": "Команды",
            },
        ),
        migrations.AddConstraint(
            model_name="usercontacts",
            constraint=models.CheckConstraint(
                check=models.Q(("user_from", models.F("user_to")), _negated=True),
                name="User cant follow to self",
            ),
        ),
    ]