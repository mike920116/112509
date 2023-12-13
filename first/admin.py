from django.contrib import admin

from first.models import Post, Learner, Tag, Comment, UserProfile
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 1129羿安加入使用者名稱
    list_display = ("id", "custom_title", "custom_user")  # 1129羿安使用自訂標題
    search_fields = ("title", "content")
    list_filter = ("is_public", "tags")
    def custom_title(self, obj):
        return obj.title
    custom_title.short_description = "標題"  # 修改 custom_title 在管理介面中的顯示名稱
    def custom_user(self, obj):
        return obj.user
    custom_user.short_description = "使用者名稱" 
    

@admin.register(Learner)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "custom_title")
    search_fields = ("title", "content")
    list_filter = ("is_public", "tags")
    def custom_title(self, obj):
        return obj.title
    custom_title.short_description = "標題"  # 修改 custom_title 在管理介面中的顯示名稱

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "content")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user_id", "username", "email", "password")

    def get_password(self, obj):
        return obj.password
    get_password.short_description = 'Password'
    

# 2023/06/01
# @admin.register(UserLogin)
# class UserLoginAdmin(admin.ModelAdmin):
#     list_display = ("id", "email", "password")
