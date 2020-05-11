from django.conf.urls import url
from django.urls import path

from apps.organizations.views import OrgView, AddAsk

urlpatterns = [
    # 配置授课机构列表展示
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddAsk.as_view(), name='list'),
]
