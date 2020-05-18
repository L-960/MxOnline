import xadmin
from apps.courses.models import *


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)


# 不用继承admin.ModelAdmin，
class CourseAdmin(object):
    # 显示字段
    list_display = ["id", "name", "desc", "learn_times", "degree"]
    # 搜索字段
    search_fields = ["name", "desc"]
    # 筛选字段
    list_filter = ["id", "name", "desc", "learn_times", "degree"]


class LessonAdmin(object):
    # 显示字段
    list_display = ["id", "course", "name", "learn_times"]
    # 搜索字段
    search_fields = ["id", "course", "name", "learn_times"]
    # 筛选字段
    list_filter = ["id", "course", "name", "learn_times"]


class VideoAdmin(object):
    # 显示字段
    list_display = ["id", "lesson", "name", "url"]
    # 搜索字段
    search_fields = ["id", "lesson", "name", "url"]
    # 筛选字段
    list_filter = ["id", "lesson", "name", "url"]


class CourseResourceAdmin(object):
    # 显示字段
    list_display = ["id", "course", "name", "file"]
    # 搜索字段
    search_fields = ["id", "course", "name", "file"]
    # 筛选字段
    list_filter = ["id", "course", "name", "file"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
