from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

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


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "註冊帳號成功")
            return redirect('post_list')  # 將此行修改為你的視圖名稱或URL
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) #我們使用了 AuthenticationForm 表單來處理登入的相關表單驗證和登入操作。
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # 如果表單驗證成功，則使用 auth_login 函數將用戶登入，並顯示成功訊息。
            messages.success(request, "登入成功")
            return redirect('post_list')  # 將此行修改為你視圖名稱或URL
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})