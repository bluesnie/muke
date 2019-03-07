# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/2/23 13:05'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse

# inline模式，只能一层嵌套，不能多层嵌套，但可以多个
class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    """
    课程管理器
    """
    # 显示的字段，还可以显示函数，可以加入model中定义的函数如获取章节数：get_lesson_nums,go_to
    list_display = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'get_lesson_nums', 'go_to']
    # 搜索功能
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']

    # ico图标
    model_icon = 'fa fa-file'

    # 排序规则
    ordering = ['-click_nums']

    # 设置某些字段为只读
    readonly_fields = ['click_nums']

    # 设置某些字段不显示,和上面的设置会冲突，所以某个字段只能设置其中一个
    exclude = ['fav_nums']

    # 展示页面中直接修改功能
    list_editable = ['degree','desc']

    # inlines 设置
    inlines = [LessonInline, CourseResourceInline]

    # 自定义刷新时间,配置多个页面中可选
    refresh_times = [3, 5]

    # 插件配置
    # 1、指明某个字段用的是什么样式，下面就是指明detail是ueditor样式
    style_fields = {"detail": "ueditor"}

    # 2、导入Excel插件为True开启(有问题，待解决)
    # import_excel = True

    # 重载方法过滤课程
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计机构的课程数
        obj = self.new_obj
        # 查询前先保存才能增加新增的数量
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)

class BannerCourseAdmin(object):
    """
    轮播课程管理器，和上面的课程管理器管理的是同一张表
    """
    list_display = ['name', 'course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                     'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    model_icon = 'fa fa-file'
    # 排序规则
    ordering = ['-click_nums']
    # 设置某些字段为只读
    readonly_fields = ['click_nums']
    # 设置某些字段不显示,和上面的设置会冲突，所以某个字段只能设置其中一个
    exclude = ['fav_nums']
    # inlines 设置
    inlines = [LessonInline, CourseResourceInline]

    # 重载方法过滤课程
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time'] #course__name外键设置
    model_icon = 'fa fa-file-o'


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']#course__name外键设置
    model_icon = 'fa fa-file-video-o'



class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']
    model_icon = 'fa fa-file-archive-o'




xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
