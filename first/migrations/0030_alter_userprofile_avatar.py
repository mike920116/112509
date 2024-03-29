# Generated by Django 4.1.7 on 2023-12-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0029_userprofile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="avatars/%Y/%m/%d/"
            ),
        ),
    ]
