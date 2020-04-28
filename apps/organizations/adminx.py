import xadmin

from apps.organizations.models import *


class CityAdmin(object):
    list_display = [
        'id', 'name', 'desc'
    ]
    search_fields = [
        'id', 'name', 'desc'
    ]
    list_filter = [
        'id', 'name', 'desc'
    ]


class CourseOrgAdmin(object):
    list_display = [
        'id', 'name', 'city', 'category', 'org'
    ]
    search_fields = [
        'id', 'name', 'city', 'category', 'org'
    ]
    list_filter = [
        'id', 'name', 'city', 'category', 'org'
    ]


class TeacherAdmin(object):
    list_display = [
        'id', 'name', 'org', 'work_years', 'teaching_trait'
    ]
    search_fields = [
        'id', 'name', 'org', 'work_years', 'teaching_trait'
    ]
    list_filter = [
        'id', 'name', 'org', 'work_years', 'teaching_trait'
    ]


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
