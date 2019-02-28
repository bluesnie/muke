# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course
from operation.models import UserFavorite

class CourseListView(View):
    """
    课程列表页
    """
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = all_courses.order_by('-click_nums')[:3]
        # 课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                # 最热门
                all_courses = all_courses.order_by('-click_nums')
            if sort == 'students':
                #参与人数
                all_courses = all_courses.order_by('-students')
        # 对课程进行翻页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 传3个参数，第二个参数是显示每页数目
        p = Paginator(all_courses, 6, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses':courses,
            'sort':sort,
            'hot_courses':hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums += 1
        course.save()

        # 判断用户是否收藏
        has_course_fav = False
        has_org_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_course_fav = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_org_fav = True

        # 相关课程推荐
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []

        return render(request, 'course-detail.html', {
            'course':course,
            'relate_courses':relate_courses,
            'has_course_fav':has_course_fav,
            'has_org_fav':has_org_fav,
        })


class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, 'course-video.html', {
            'course': course,
        })