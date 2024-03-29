# Generated by Django 4.1.7 on 2023-11-17 08:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("first", "0015_rename_login_userlogin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signup",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="signup",
            name="fname",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="signup",
            name="password",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="signup",
            name="uname",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="userlogin",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="userlogin",
            name="password",
            field=models.CharField(max_length=100),
        ),
    ]
