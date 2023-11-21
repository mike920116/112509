from django import forms
from django.contrib.auth.models import User
from first.models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('title', 'content')
        tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="Select a Tag",
        required=False,
    )

class PostDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
         required=True,
        label="你確定要刪除這篇文章嗎？真的會消失喔！！！",
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("post",)

class CommentDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="你確定要刪除這則留言嗎？真的會消失喔！！！",
    )

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"