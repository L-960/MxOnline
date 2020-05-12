import random

from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from pure_pagination import Paginator

from apps.courses.models import *
# Create your views here.
from django.views.generic.base import View


class CourseView(View):
    def get(self, request, *args, **kwargs):
        # 先获得所有课程信息,order_by默认升序，改成降序
        all_courses = Course.objects.all().order_by('id').order_by('-add_time')
        # 获取热门课程，前三个
        hot_courses = Course.objects.order_by('-click_nums')[:3]
        # 获取sort,默认为空
        sort = request.GET.get('sort', '')
        # 如果sort存在，按照条件排序
        if sort:
            if sort == 'hot':
                all_courses = all_courses.order_by('-fav_nums')
            elif sort == 'students':
                all_courses = all_courses.order_by('-students')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, request=request, per_page=6)

        courses = p.page(page)

        return render(request, 'course-list.html', context={
            'courses': courses,
            'title': '公开课',
            'sort': sort,
            'hot_courses': hot_courses,
        })


def coursetest(request):
    # 批量创建source
    # for i in range(500):
    #     course = Course()
    #     course.name = 'django课程{}'.format(i+1)
    #     course.desc = 'django课程描述{}'.format(i+1)
    #     course.learn_times = random.randint(0,500)
    #     course.degree = 'cj'
    #     course.students = random.randint(0,100)
    #     course.fav_nums = random.randint(0,50)
    #     course.click_nums = random.randint(0,5000)
    #     course.notice = '课程公告{}'.format(i+1)
    #     course.category = '课程类别{}'.format(i+1)
    #     course.tag = '课程标签{}'.format(i+1)
    #     course.youneed_know = '你要知道{}'.format(i+1)
    #     course.teacher_tell = '老师告诉你{}'.format(i+1)
    #     course.image = 'courses/2020/05/一起学.png'
    #     course.save()

    # #  批量创建课程章节
    # courses = Course.objects.all().order_by('id')
    # for course in courses:
    #     for i in range(10):
    #         lesson = Lesson()
    #         lesson.course = course
    #         lesson.name = course.name + f'_章节{i+1}'
    #         lesson.learn_times = random.randint(0, 500)
    #         lesson.save()
    return HttpResponse('create ok')
