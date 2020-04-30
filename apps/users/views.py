from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View
from apps.users.form import *


def index(request):
    return render(request, 'index.html')


# def login(request):
#     pass


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        """
        用户登陆验证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 实例化LoginForm
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 通过用户名密码查询用户是否存在,获取表单中内容
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]

            # 去数据库比对，并且返回对象
            user = authenticate(username=user_name, password=password)
            # 判断user对象是否存在
            if user is not None:
                #  不为空，证明查询到了用户,返回首页
                login(request, user)
                return redirect(reverse('index'))
                # return render(request, 'index.html', context={'is_login': True})
            else:
                #  未查询到用户，重新登陆
                return render(request, 'login.html', context={
                    "msg": '用户名密码错误',
                    "login_form": login_form,
                })
        else:
            #  未查询到用户，重新登陆
            return render(request, 'login.html', context={
                "msg": '未查询到用户，重新登陆',
                "login_form": login_form,
            })
