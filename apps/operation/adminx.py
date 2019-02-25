# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/23 13:44'

import xadmin

from .models import UserAsk, UserCourse, CourseComments, UseMessage, UserFavorite


class UserAskAdmin(object):
    list_display = ['name', 'tel', 'course_name', 'add_time']
    search_fields = ['name', 'tel', 'course_name']
    list_filter = ['name', 'tel', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UseMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UseMessage, UseMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)