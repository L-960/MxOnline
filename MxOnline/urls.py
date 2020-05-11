"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import xadmin
from django.views.generic import TemplateView

from apps.courses import views
from apps.courses.views import CourseView
from apps.organizations.views import OrgView
from apps.users.views import LoginView
from django.conf.urls import url
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # path('', views.index),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),

    # 配置公开课的url
    path('courselist/', CourseView.as_view(), name='course_list'),
    url(r'^coursetest/', views.coursetest, name='coursetest'),

    # 配置授课机构子路由
    url(r'^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),
]
