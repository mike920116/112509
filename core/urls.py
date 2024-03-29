"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import Group


from core.views import my_path, add, minus, multiplied_by, divided_by
from first.views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    post_comment,
    learner_list,
    learner_detail,
    learner_create,
    learner_update,
    learner_delete,
    learner_comment,
    comment_update,
    comment_delete,
    learnercomment_update,
    learnercomment_delete,

    # sync_user_data,

    signup,
    login,
    profile,
    
    logout,
)
# 2023/05/26
# admin/的內容
admin.site.site_header = '管理員後台'
admin.site.site_title = '管理員後台'
admin.site.index_title = '網站管理'
# 羿安：如果不需要用時可以取消註解
# admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用者註冊畫面
    path('signup/', signup, name='signup'),
    # 使用者登入畫面
    path('login/', login, name='login'),
    path('profile/<int:user_id>/', profile, name='profile'),
    path('add/<int:n1>/<int:n2>/', add),
    path('minus/<int:n1>/<int:n2>/', minus),
    path('multiplied_by/<int:n1>/<int:n2>/', multiplied_by),
    path('divided_by/<int:n1>/<int:n2>/', divided_by),
    path('post-list/', post_list, name='post_list'),
    path('post-detail/<int:post_id>/', post_detail, name='post_detail'),
    path('post-create/', post_create, name='post_create'),
    path('post-update/<int:post_id>', post_update, name='post_update'),
    path('post-delete/<int:post_id>/', post_delete, name='post_delete'),
    path("post-comment/<int:post_id>/", post_comment, name="post_comment"),
    path('learner-list/', learner_list, name='learner_list'),
    path('learner-detail/<int:learner_id>/', learner_detail, name='learner_detail'),
    path('learner-create/', learner_create, name='learner_create'),
    path('learner-update/<int:learner_id>', learner_update, name='learner_update'),
    path('learner-delete/<int:learner_id>/', learner_delete, name='learner_delete'),
    path("learner-comment/<int:learner_id>/", learner_comment, name="learner_comment"),

    # path('sync_user_data/<int:user_id>/', sync_user_data, name='sync_user_data'),

    #使用者帳號查看和編輯


    path('logout/', logout, name='logout'),
    
    #--------留言
    path('comment-update/<int:comment_id>', comment_update, name='comment_update'),
    path('comment-delete/<int:comment_id>/', comment_delete, name='comment_delete'),

    path('learnercomment-update/<int:learnercomment_id>', learnercomment_update, name='learnercomment_update'),
    path('learnercomment-delete/<int:learnercomment_id>/', learnercomment_delete, name='learnercomment_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
