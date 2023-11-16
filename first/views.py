# views.py的用途主要用於新創建的表單來處理登入請求。

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

from first.models import Post, Comment
from first.forms import (
    PostForm,
    PostDeleteConfirmForm,
    CommentForm,
    CommentDeleteConfirmForm,
)
def post_list(request):

    posts = Post.objects.prefetch_related("tags")
    if "tag_id" in request.GET:
        posts = posts.filter(tags__id=request.GET["tag_id"])
        
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, '文章建立成功')
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
        comment.save()

        messages.success(request, "留言成功")
        return redirect("post_detail", post_id)

    return render(request, "post_comment.html", {"form": form})

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

# UserCreationForm
from first.forms import SignupForm
def signup(request):
    print('request', request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("hello")
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("save hello")
            messages.success(request, "註冊帳號成功")
            return redirect('login')  # 將跳轉到主畫面
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request, data=request.POST) #我們使用了 AuthenticationForm 表單來處理登入的相關表單驗證和登入操作。
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # remember_me = form.cleaned_data['remember_me']
            remember_me = request.POST.get('remember_me')

            # 使用 Django 內建的 authenticate 函數進行驗證
            user = authenticate(request, username=username, password=password)
            print('user', user)
            if user is not None:
                # 使用 Django 內建的 login 函數進行登入
                auth_login(request, user)
                if remember_me:
                    request.session.set_expiry(0)  # 設定 session 永久保存
                else:
                    request.session.set_expiry(120)  # 設定 session 120 秒後過期
                messages.success(request, "登入成功")
                #登入後跳去哪個html
                return redirect('topic')
            else:
                messages.error(request, "登入失敗，請檢查用戶名和密碼")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# def about(request):
#     return render(request, 'about.html')

# def experience(request):
#     return render(request, 'experience.html')

def education(request):
    return render(request, 'education.html')

def topic(request):
    return render(request, 'topic.html')

def course(request):
    return render(request, 'course.html')

def answer(request):
    return render(request, 'answer.html')

def logout(request):
    auth_logout(request)
    return redirect('topic')
