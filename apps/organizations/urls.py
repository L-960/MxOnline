from django.conf.urls import url
from django.urls import path

from apps.organizations.views import *

urlpatterns = [
    # 配置授课机构列表展示
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddAsk.as_view(), name='add_ask'),
    # 讲师
    url(r'^teachers/$', TeacherListView.as_view(), name='teachers'),
    url(r'^teachers/(?P<teacher_id>\d+)$', TeacherDetail.as_view(), name='teacher_detail'),
]
