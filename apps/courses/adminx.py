import xadmin
from apps.courses.models import *


class CourseAdmin(object):
    # 显示属性字段
    list_display = [
        'id', 'name', 'desc', 'learn_times', 'degree'
    ]
    # 搜素字段
    search_fields = [
        'name', 'desc',
    ]
    # 筛选
    list_filter = [
        'id', 'name', 'desc', 'learn_times', 'degree'
    ]


class LessonAdmin(object):
    list_display = [
        'id', 'name', 'course',
    ]
    search_fields = [
        'name', 'course'
    ]
    list_filter = [
        'id', 'name', 'course',
    ]


class VideoAdmin(object):
    list_display = [
        'id', 'name', 'lesson'
    ]
    search_fields = [
        'name', 'lesson'
    ]
    list_filter = [
        'id', 'name', 'lesson'
    ]


class CourseResourceAdmin(object):
    list_display = [
        'id', 'name', 'course'
    ]
    search_fields = [
        'name', 'course'
    ]
    list_filter = [
        'id', 'name', 'course'
    ]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
