from django.contrib import admin


# 因为用户表相对来说都是系统中存在的， django内置了一个UserAdmin对显示用户信息做了优化
from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
admin.site.register(UserProfile, UserAdmin)

