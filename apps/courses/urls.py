from django.conf.urls import url
from apps.courses.views import CourseView

urlpatterns = [
    # 配置公开课路由
    url(r'^list/$', CourseView.as_view(), name='list'),
]
