import xadmin
from apps.courses.models import Course


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


xadmin.site.register(Course, CourseAdmin)
