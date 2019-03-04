# _*_encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/27 10:47'

from django.urls import path, include, re_path
from organization.views import OrgListView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, UserFavView
from .views import TeacherListView, TeacherInfoView

app_name = 'organization'

urlpatterns = [
    # 课程机构列表页
    path('list/', OrgListView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    re_path('org_teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),

    # 机构收藏
    path('add_fav/', UserFavView.as_view(), name='add_fav'),

    # 机构讲师
    path('teacher/list/', TeacherListView.as_view(), name='teacher_list'),
    # 讲师详情页
    re_path('teacher/info/(?P<teacher_id>\d+)/', TeacherInfoView.as_view(), name='teacher_info'),
]