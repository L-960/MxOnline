from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.operations.forms import UserFavForm, CourseComments, CommentForm
from apps.operations.models import UserFavorite, Banner
from apps.courses.models import Course
from apps.organizations.models import CourseOrg
from apps.organizations.models import Teacher


class AddFavView(View):
    '''
    用户收藏实现
    先判断用户是否登陆
    '''

    def post(self, request, *args, **kwargs):
        # 如果没登陆
        if not request.user.is_authenticated:
            return JsonResponse({
                'status': 'fail',
                'msg': '用户未登陆',
            })

        user_fav_form = UserFavForm(request.POST)
        #  如果表单合法
        if user_fav_form.is_valid():

            fav_id = user_fav_form.cleaned_data["fav_id"]
            fav_type = user_fav_form.cleaned_data["fav_type"]
            #  判断用户是否已经收藏
            #  是否存在记录
            existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
            if existed_records:
                # 如果已经收藏，把收藏这条信息删除
                existed_records.delete()

                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '收藏',
                })

            else:
                user_fav = UserFavorite()
                user_fav.user = request.user
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.save()
                return JsonResponse({
                    'status': 'success',
                    'msg': '已收藏',
                })

        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '参数错误',
            })


class CommentView(View):
    '''
    用户评论
    '''

    # 先判断用户是否登陆
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({
                'status': 'fail',
                'msg': '用户未登陆',
            })
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            course_comment = CourseComments()
            user = request.user
            course = comment_form.cleaned_data["course"]
            comments = comment_form.cleaned_data["comments"]
            course_comment.user = user
            course_comment.course = course
            course_comment.comments = comments
            course_comment.save()
            return JsonResponse({
                'status': 'success',
                'msg': '',
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '表单不合法',
            })


class IndexView(View):
    def get(self, request):
        '''
        首页请求
        '''
        # 轮播图banner加载
        banners = Banner.objects.all().order_by("index")[:4]
        # 公开课加载(除去banner课程)
        courses = Course.objects.filter(is_banner=False)[:6]
        # 公开课小banner加载
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        # 机构加载
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', context={
            'banners': banners,
            'courses': courses,
            'course_orgs': course_orgs,
            'banner_courses': banner_courses,
        })
