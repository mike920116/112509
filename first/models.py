#當你在 models.py 文件中定義或更改模型後，使用 makemigrations 和 migrate 命令，Django 將同步這些更改到資料庫。

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    is_public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')

    #2023/4/29
    # tags = models.ManyToManyField(to='Tag')

    # 2023/5/6
    tags = models.ManyToManyField(to="Tag", blank=True)
    image = models.ImageField(upload_to="posts/%Y/%m/%d/", null=True, blank=True)
    # video = models.FileField(upload_to="posts/%Y", null=True, blank=True)
    # null -> 可以存放 null 到資料庫中
    # blank -> 這個欄位是可以不填寫的

    # 自動產生的欄位
    # comment_set => 代表了與 Comment 資料表的關聯（<model>_set）

    def __str__(self):
        return self.title
    

class Learner(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    is_public = models.BooleanField(default=True)

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')

    #2023/4/29
    # tags = models.ManyToManyField(to='Tag')

    # 2023/5/6
    tags = models.ManyToManyField(to="Tag", blank=True)
    image = models.ImageField(upload_to="posts/%Y/%m/%d/", null=True, blank=True)
    video = models.FileField(upload_to="learners/%Y/%m/%d/", null=True, blank=True)
    # null -> 可以存放 null 到資料庫中
    # blank -> 這個欄位是可以不填寫的

    # 自動產生的欄位
    # comment_set => 代表了與 Comment 資料表的關聯（<model>_set）

    def __str__(self):
        return self.title
    
#2023/4/29
class Comment(models.Model):
    #---------------#TextField多行文字
    content = models.TextField(max_length=500)
    post = models.ForeignKey(to = Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    # 自動產生的欄位
    # post_id => 代表管連到的 Post 的 PK （<fk>_id）

#2023/4/29
class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

# class UserLogin(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.email
    
# class Signup(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)  # 注意：實際應用中應使用加密的密碼存儲方式
#     is_teacher = models.BooleanField(default=False)
#     gmail = models.EmailField(blank=True, null=True)

#     def __str__(self):
#         return self.user.username
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')
    account_type = models.CharField(max_length=100, default='學生')
    gmail = models.EmailField()
    private_password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username