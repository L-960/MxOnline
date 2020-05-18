import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from pure_pagination import Paginator

from apps.courses.models import *
# Create your views here.
from django.views.generic.base import View
from apps.operations.models import *


class CourseListView(View):
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


class CourseDetailView(View):
    def get(self, request, course_id):
        '''
        获取课程详情页
        :param request:
        :return:
        '''
        # 根据id查询课程详情
        course = Course.objects.get(pk=int(course_id))
        # 当前course点击次数+1
        course.click_nums += 1
        course.save()

        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org = True

        return render(request, 'course-detail.html', context={
            'course': course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
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

    # 增加课程章节
    # courses = Course.objects.all()
    # for course in courses:
    #     for i in range(8):
    #         lesson = Lesson()
    #         lesson.course = course
    #         lesson.name = f'课程章节测试{i+1}'
    #         lesson.save()

    # 章节视频测试

    # lessons = Lesson.objects.all()
    # for lesson in lessons:
    #     for i in range(3):
    #         video = Video()
    #         video.lesson = lesson
    #         video.name = f'视频资源{i+1}'
    #         video.learn_times = 10 * (i + 1) + 21
    #         video.url = '测试url'
    #         video.save()


    # 资源测试
    # courses = Course.objects.all()
    # for course in courses:
    #     resource = CourseResource()
    #     for i in range(3):
    #         resource.course = course
    #         resource.name = f'资源下载测试{i+1}'
    #         resource.file = 'courses/resourse/2020/05/GitHubDesktop.exe'
    #         resource.save()

    return HttpResponse('create ok')


class CourseLessonView(LoginRequiredMixin, View):
    """
        章节信息
    """
    login_url = '/login/'

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        # 点击到课程 的详情就记录一次点击数
        course.click_nums += 1
        course.save()

        # 查询资料信息
        course_resource = CourseResource.objects.filter(course=course)

        return render(request, 'course-video.html', {
            "course": course,
            "course_resource": course_resource,
        })
