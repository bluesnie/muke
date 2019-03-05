# _*_encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/3/4 15:17'

from django.urls import path, include, re_path
from .views import UserInfoView, UploadImageView,UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MycoursesView,MyfavOrgView, MyfavTeacherView, MyfavCourseView, MymessageView

app_name = 'users'

urlpatterns = [
    # 用户个人中心页
    path('info/', UserInfoView.as_view(), name='user_info'),

    # 修改头像
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name='update_pwd' ),

    # 发送修改邮箱验证码
    path('sendemail_code/', SendEmailCodeView.as_view(), name='sendemail_code' ),

    # 修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name='update_email' ),

    # 我的课程
    path('mycourses/', MycoursesView.as_view(), name='mycourses'),

    # 我收藏的课程机构
    path('myfav/org/', MyfavOrgView.as_view(), name='myfav_org'),

    # 我收藏的课程讲师
    path('myfav/teacher/', MyfavTeacherView.as_view(), name='myfav_teacher'),

    # 我收藏的课程
    path('myfav/course/', MyfavCourseView.as_view(), name='myfav_course'),

    # 我的消息
    path('mymessage/', MymessageView.as_view(), name='mymessage'),
]