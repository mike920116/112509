from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from first.models import Post, Comment, Tag, Learner, UserProfile, LearnerComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('title', 'content')
        exclude = ("user",)
        tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="Select a Tag",
        required=False,
    )
        
class PostDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
         required=True,
        label="你確定要刪除這篇題目嗎？真的會消失喔！！！",
    )

class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'
        # fields = ('title', 'content')
        exclude = ("user",)
        tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="Select a Tag",
        required=False,
    )
class LearnerDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
         required=True,
        label="你確定要刪除這篇教材嗎？真的會消失喔！！！",
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("post", "user")

class LearnerCommentForm(forms.ModelForm):
    class Meta:
        model = LearnerComment
        # fields = "__all__"
        exclude = ("learner", "user")

class CommentDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="你確定要刪除這則留言嗎？真的會消失喔！！！",
    )

class LearnerCommentDeleteForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="你確定要刪除這則留言嗎？真的會消失喔！！！",
    )

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_teacher = forms.BooleanField(required=False)
    gmail = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileUpdateForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput, label='Current Password')

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'current_password']
        widgets = {'password':forms.PasswordInput()}
# class ProfileForm(forms.ModelForm):
    
#     class Meta:
#         model = UserProfile
#         fields = ['avatar', 'account_type', 'gmail', 'private_password']