# _*_ encoding: utf-8 _*_
"""muke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, IndexView
from muke.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>\w+.*)/', ActiveUserView.as_view(), name="user_active"),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>\w+.*)/', ResetView.as_view(), name="reset_pwd"),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 课程机构url配置
    path('org/', include('organization.urls', namespace='org')),

    # 课程url配置
    path('course/', include('courses.urls', namespace='course')),

    # 用户url配置
    path('users/', include('users.urls', namespace='users')),

    # 配置上传文件的访问处理函数
    re_path('media/(?P<path>.*)', serve, {"document_root":MEDIA_ROOT}),

    # 配置静态文件的访问处理函数
    # re_path('static/(?P<path>.*)', serve, {"document_root":STATIC_ROOT}),

]

# 配置404等错误处理函数(配置后出错,待解决,注释)
# handler404 = 'users.views.page_not_found'
# handler403 = 'users.views.page_forbidden'
# handler500 = 'users.views.server_error'
