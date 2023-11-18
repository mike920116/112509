from django.contrib import admin

from first.models import Post, Tag, Comment, UserLogin
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "content")
    list_filter = ("is_public", "tags")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "content")

# 2023/06/01
@admin.register(UserLogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password")
