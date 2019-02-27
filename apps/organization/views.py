# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import CourseOrg, CityDict
from .forms import UserAskForm

# Create your views here.


class OrgListView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构排行
        hot_orgs = all_orgs.order_by('click_nums')[:3]
        # 城市
        all_citys = CityDict.objects.all()

        # 取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 学习人数，课程数筛选
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            if sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        # 筛选完载统计
        org_nums = all_orgs.count()
        # 对课程机构进行翻页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 传3个参数，第二个参数是显示每页数目
        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)
        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "all_citys":all_citys,
            "org_nums":org_nums,
            "city_id":city_id,
            "category":category,
            "hot_orgs":hot_orgs,
            "sort":sort

        })


class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, requeset):
        userask_form = UserAskForm(requeset.POST)
        if userask_form.is_valid():
            # 因为是modelform继承了model属性，可以直接save,commit为true提交保存
            user_ask = userask_form.save(commit=True)
            # 此时是异步操作返回json,不是返回页面刷新
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 反向取出课程和教师
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
        })


class OrgCourseView(View):
    """
    机构课程页
    """
    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 反向取出课程
        all_courses = course_org.course_set.all()
        return render(request, 'org-detail-course.html', {
            'all_courses':all_courses,
            'course_org':course_org,
            'current_page': current_page,
        })


class OrgDescView(View):
    """
    机构介绍页
    """
    def get(self, request, org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            'course_org':course_org,
            'current_page': current_page,
        })



class OrgTeacherView(View):
    """
    机构教师页
    """
    def get(self, request, org_id):
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 反向取出课程和教师
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page': current_page,
        })
