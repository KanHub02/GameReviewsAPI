# Generated by Django 4.1.2 on 2022-11-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_ip_user_views"),
        ("media_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="views",
            field=models.ManyToManyField(to="users.ip"),
        ),
    ]