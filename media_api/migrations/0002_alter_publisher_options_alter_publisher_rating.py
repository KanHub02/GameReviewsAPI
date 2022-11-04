# Generated by Django 4.1.2 on 2022-11-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("media_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="publisher",
            options={"verbose_name": "Издатель", "verbose_name_plural": "Издатели"},
        ),
        migrations.AlterField(
            model_name="publisher",
            name="rating",
            field=models.IntegerField(
                choices=[(1, "*"), (2, "**"), (3, "***"), (4, "****"), (5, "*****")],
                default=0.0,
            ),
        ),
    ]