from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from apps.operations.models import UserCourse, UserFavorite
from apps.organizations.models import CourseOrg
from apps.users.form import LoginForm, ChangePwdForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from apps.users.models import UserProfile


# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return reverse('index')
        next = request.GET.get("next", '')

        return render(request, 'login.html', context={
            'next': next,
        })

    def post(self, request, *args, **kwargs):
        """
        用户登录验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 实例化 LoginForm

        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            # 用于通过用户名和密码查询用户是否存在
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
            # 判断user对象是否存在
            if user is not None:
                # 不为空， 证明查询到了用户
                login(request, user)
                # 取一下next值
                next = request.GET.get("next", "")
                if next:
                    return HttpResponseRedirect(next)
                # 重定向到网站首页
                return HttpResponseRedirect(reverse("index"))
            else:
                # 未查询到用户，要求重新登录,仍然返回login界面
                return render(request, 'login.html', {"msg": "用户名密码错误", "login_form": login_form})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # 重定向到网站首页
        return HttpResponseRedirect(reverse("index"))


class UserInfoView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        current_page = 'info'
        return render(request, 'usercenter-info.html', context={
            'current_page': current_page,
        })


# class MyCourseView(LoginRequiredMixin, View):
#     login_url = '/login/'
#
#     def get(self, request):
#         current_page = 'mycourse'
#
#         mycourse = UserCourse.objects.filter(user=request.user)
#
#         return render(request, 'usercenter-mycourse.html', context={
#             'current_page': current_page,
#             'mycourse': mycourse,
#         })
class MyFavOrgView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        ''''''
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)

        org_list = []

        for fav_org in fav_orgs:
            org = CourseOrg.objects.get(id=fav_org.fav_id)
            org_list.append(org)

        return render(request, 'usercenter-fav-org.html', context={
            'current_page': 'myfav',
            'org_list': org_list,
        })


class MyFavCourseView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'usercenter-fav-course.html', context={
            'current_page': 'myfav',
        })


class MyFavTeacherView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'usercenter-fav-teacher.html', context={
            'current_page': 'myfav',
        })


class ChangePwdView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        pwd_form = ChangePwdForm(request.POST)
        if pwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            user = request.user
            user.set_password(pwd1)
            user.save()
            return JsonResponse({
                "status": "success",
            })
        else:
            return JsonResponse(pwd_form.errors)
