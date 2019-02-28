# _*_encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/28 11:07'

from django.urls import path, include, re_path

from .views import CourseListView, CourseDetailView, CourseInfoView

app_name = 'courses'

urlpatterns = [
    # 课程列表页
    path('list/', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),

    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),

]