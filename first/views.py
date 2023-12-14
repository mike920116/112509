from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
import os

from first.models import Post, Comment, Tag, Learner, UserProfile, LearnerComment
from first.forms import (
    PostForm,
    PostDeleteConfirmForm,
    LearnerForm,
    LearnerDeleteConfirmForm,
    CommentForm,
    LearnerCommentForm,
    CommentDeleteConfirmForm,
    LearnerCommentDeleteForm,
    SignupForm,
    UserProfileUpdateForm
    # ProfileForm
)

def post_list(request):
    
    difficulties = Post.DIFFICULTY_CHOICES

    posts = Post.objects.prefetch_related("tags")

    query = request.GET.get('Search_query')
    selected_difficulty = request.GET.get('difficulty')
    selected_tag_id = request.GET.get('tag_id')

    if "tag_id" in request.GET and request.GET["tag_id"] != 'all':
        posts = posts.filter(tags__id=request.GET["tag_id"])
    if "tag_name" in request.GET:
        posts = posts.filter(tags__name=request.GET["tag_name"])
        
    if query:
        posts = posts.filter(Q(title__icontains=query))
    if selected_difficulty:
        posts = posts.filter(difficulty=selected_difficulty)
    # tag_id = request.GET.get('tag_id')
    # if tag_id:
    #     posts = posts.filter(tags__id=tag_id)

    all_tags = Tag.objects.all()
    selected_tag = Tag.objects.get(pk=selected_tag_id) if "tag_id" in request.GET and request.GET["tag_id"] != 'all' and selected_tag_id else None
        
    return render(request, 'post_list.html', {
        'posts': posts, 
        'difficulties': difficulties, 
        'selected_difficulty': selected_difficulty, 
        'all_tags': all_tags,
        'selected_tag': selected_tag,
        })


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=True)
        post.user = request.user
        post.save()
        messages.success(request, '題目建立成功')
        return redirect('post_list')

    return render(request, 'post_create.html', {'form': form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, '文章編輯成功')
        return redirect('post_detail', post_id)

    return render(request, 'post_update.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, '文章刪除成功')
        return redirect('post_list')

    return render(request, 'post_delete.html', {'form': form})

def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

        messages.success(request, "留言成功")
        return redirect("post_detail", post_id)

    return render(request, "post_comment.html", {"form": form})

def learner_list(request):
    
    difficulties = Learner.DIFFICULTY_CHOICES

    learners = Learner.objects.prefetch_related("tags")

    query = request.GET.get('Search_query')
    selected_difficulty = request.GET.get('difficulty')
    selected_tag_id = request.GET.get('tag_id')

    if "tag_id" in request.GET and request.GET["tag_id"] != 'all':
        learners = learners.filter(tags__id=request.GET["tag_id"])
    if "tag_name" in request.GET:
        learners = learners.filter(tags__name=request.GET["tag_name"])
        
    if query:
        learners = learners.filter(Q(title__icontains=query))
    if selected_difficulty:
        learners = learners.filter(difficulty=selected_difficulty)
    # tag_id = request.GET.get('tag_id')
    # if tag_id:
    #     posts = posts.filter(tags__id=tag_id)

    all_tags = Tag.objects.all()
    selected_tag = Tag.objects.get(pk=selected_tag_id) if "tag_id" in request.GET and request.GET["tag_id"] != 'all' and selected_tag_id else None
        
    return render(request, 'learner_list.html', {
        'learners': learners, 
        'difficulties': difficulties, 
        'selected_difficulty': selected_difficulty, 
        'all_tags': all_tags,
        'selected_tag': selected_tag,})

def learner_detail(request, learner_id):
    # post = Post.objects.get(id=post_id)
    learner = get_object_or_404(Learner, id=learner_id)
    return render(request, 'learner_detail.html', {'learner': learner})


def learner_create(request):
    form = LearnerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        learner = form.save(commit=True)
        learner.user = request.user
        learner.save()
        messages.success(request, '教材建立成功')
        return redirect('learner_list')

    return render(request, 'learner_create.html', {'form': form})

def learner_update(request, learner_id):
    learner = get_object_or_404(Learner, id=learner_id)

    form = LearnerForm(request.POST or None, request.FILES or None, instance=learner)
    if form.is_valid():
        form.save()
        messages.success(request, '文章編輯成功')
        return redirect('learner_detail', learner_id)

    return render(request, 'post_update.html', {'form': form})

def learner_delete(request, learner_id):
    post = get_object_or_404(Learner, id=learner_id)
    form = LearnerDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, '文章刪除成功')
        return redirect('learner_list')

    return render(request, 'learner_delete.html', {'form': form})

def learner_comment(request, learner_id):
    learner = get_object_or_404(Learner, id=learner_id)

    form = LearnerCommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.learner = learner
        comment.user = request.user
        comment.save()

        messages.success(request, "留言成功")
        return redirect("learner_detail", learner_id)

    return render(request, "learner_comment.html", {"form": form})

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        comment = form.save()
        messages.success(request, "留言編輯成功")
        return redirect("post_detail", comment.post_id)

    return render(request, "comment_update.html", {"form": form})


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    form = CommentDeleteConfirmForm(request.POST or None)
    if form.is_valid():
        comment.delete()
        messages.success(request, "留言刪除成功")
        return redirect("post_detail", comment.post_id)

    return render(request, "comment_delete.html", {"form": form})

def learnercomment_update(request, learnercomment_id):
    learnercomment = get_object_or_404(LearnerComment, id=learnercomment_id)

    form = LearnerCommentForm(request.POST or None, instance=learnercomment)
    if form.is_valid():
        learnercomment = form.save()
        messages.success(request, "留言編輯成功")
        return redirect("learner_detail", learnercomment.learner_id)

    return render(request, "learnercomment_update.html", {"form": form})

def learnercomment_delete(request, learnercomment_id):
    learnercomment = get_object_or_404(LearnerComment, id=learnercomment_id)

    form = LearnerCommentDeleteForm(request.POST or None)
    if form.is_valid():
        learnercomment.delete()
        messages.success(request, "留言刪除成功")
        return redirect("learner_detail", learnercomment.learner_id)

    return render(request, "learnercomment_delete.html", {"form": form})

# UserCreationForm
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # password1 = form.cleaned_data['password1']
            # password=make_password(password1)
            # signup_instance = Signup(user=user)
            # signup_instance.save()

            auth_login(request, user)
            messages.success(request, "註冊成功!!現在已成功登入。")
            return redirect('post_list')
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data.get('username')
        #     email = form.cleaned_data.get('email')
        #     raw_password = form.cleaned_data.get('password1')
        #     is_teacher = form.cleaned_data.get('is_teacher')
        #     gmail = form.cleaned_data.get('gmail')
        #     user = authenticate(username=username, email=email, password=raw_password)
        #     login(request)
        #     print("save hello")
        #     return redirect('login')  # 將跳轉到主畫面
            
        
        # if is_teacher and gmail:
        #         # Query the database to check if the provided Gmail exists
        #         if Signup.objects.filter(gmail=gmail).exists():
        #             # Save the user with the new fields
        #             user = form.save(commit=False)
        #             user.is_teacher = True
        #             user.save()

        #             # Additional logic if needed

        #             messages.success(request, '註冊成功')
        #             return redirect('login')
        #         else:
        #             messages.error(request, '查無此教師帳戶!!')
        # else:
        #         # Save the user without the teacher-specific fields
        #     form.save()

        #     messages.success(request, '註冊成功')
        #     return redirect('login')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request, data=request.POST) #我們使用了 AuthenticationForm 表單來處理登入的相關表單驗證和登入操作。
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # remember_me = form.cleaned_data['remember_me']
            remember_me = request.POST.get('remember_me')

            # 使用 Django 內建的 authenticate 函數進行驗證
            user = authenticate(request, username=username, password=password)
            # print('user', user)
            # print(user is not None)
            if user is not None:
                # 使用 Django 內建的 login 函數進行登入
                auth_login(request, user)
                # if remember_me:
                #     request.session.set_expiry(0)  # 設定 session 永久保存
                # else:
                #     request.session.set_expiry(120)  # 設定 session 120 秒後過期
                messages.success(request, "登入成功")
                #登入後跳去哪個html
                return redirect('post_list')
            else:
                messages.error(request, "登入失敗，請檢查用戶名和密碼")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

def profile(request, user_id):

    # 1. 檢索User模型實例
    user_auth = get_object_or_404(User, id=user_id)

    # 2. 獲取欄位的值
    username = user_auth.username
    email = user_auth.email
    password = user_auth.password  

    # 3. 創建UserProfile模型實例
    user_profile, created = UserProfile.objects.get_or_create(
        user=user_auth
        )

    # 4. 設置欄位的值
    if not created:
        user_profile.username = username
        user_profile.email = email
        user_profile.password = password
        # messages.success(request, "用戶資料同步完成。")

    # 5. 保存UserProfile透過 user_profile.save()
    # if request.method == 'POST':
    #     avatar = request.FILES.get('avatar')
    #     if avatar:
    #         user_profile.avatar = avatar
    #         user_profile.save()
    #         messages.success(request, "頭像已更新。")
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        if avatar:
            old_user_profile = UserProfile.objects.get(pk=user_profile.pk)
            if old_user_profile.avatar:
            # 刪除舊的頭像文件
                old_user_profile.avatar.delete(save=False)
            user_profile.avatar = avatar
            user_profile.save()
            messages.success(request, "頭像已更新。")
        form = UserProfileUpdateForm(instance=user_profile)

        if form.is_valid():
            current_password = form.cleaned_data.get('current_password')
            if user_auth.check_password(current_password):

                user_auth.username = form.cleaned_data['username']
                user_auth.email = form.cleaned_data['email']
                user_auth.set_password(form.cleaned_data['password'])
                user_auth.save()
                
                user_profile = form.save(commit=True)
                user_profile.user = user_auth
                user_profile.save()

                auth_login(request, user_auth)

                messages.success(request, "資料已更新。")
                return redirect('profile', user_id)
            else:
                messages.error(request, "當前密碼不正確，請重新輸入。")
        # else:
        #     messages.error(request, "表單填寫有誤，請檢查並重新提交。")
    else:
        form = UserProfileUpdateForm(instance=user_profile)

    
    
    # if request.method == 'GET':
    #     messages.success(request, "已成功提交變更")
    return render(request, 'profile.html', {"user_profile": user_profile, 'form': form})
    # user_profile = request.user.userprofile
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=user_profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    # else:
    #     form = ProfileForm(instance=user_profile)

    # return render(request, 'profile.html', {'form': form})
    # -------------------------------------------------------------
    # user_profile = get_object_or_404(User, user=request.user)
    # form = ProfileForm(instance=user_profile)

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=user_profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    
    # return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})


# def sync_user_data(request, user_id):
#     # 1. 檢索User模型實例
#     user_instance = get_object_or_404(User, id=user_id)

#     # 2. 獲取欄位的值
#     username = user_instance.username
#     email = user_instance.email
#     password = user_instance.password  # Note: You may need to handle password hashing properly

#     # 3. 創建UserProfile模型實例
#     user_profile = UserProfile(user=user_instance)

#     # 4. 設置欄位的值
#     user_profile.username = username
#     user_profile.email = email
#     user_profile.password = password  # Note: You may need to handle password hashing properly

#     # 5. 保存UserProfile模型實例
#     user_profile.save()

#     messages.success(request, "用戶資料複製完成。")
#     return redirect('post_list')