# Generated by Django 4.1.7 on 2023-11-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0019_learner"),
    ]

    operations = [
        migrations.AddField(
            model_name="learner",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="posts/%Y"),
        ),
    ]