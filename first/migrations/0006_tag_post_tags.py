# Generated by Django 4.1.7 on 2023-04-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0005_comment"),
    ]

    operations = [
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
                ("name", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="first.tag"),
        ),
    ]
