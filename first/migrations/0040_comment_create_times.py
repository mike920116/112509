# Generated by Django 4.1.7 on 2023-12-15 01:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0039_remove_comment_times"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="create_times",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
