from django.conf.urls import url

from apps.courses import views
from apps.courses.views import *

urlpatterns = [
    # 配置公开课路由
    url(r'^list/$', CourseListView.as_view(), name='list'),
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<course_id>\d+)/lesson/$', CourseLessonView.as_view(), name='lesson'),
    url(r'^test/', views.coursetest),
]
