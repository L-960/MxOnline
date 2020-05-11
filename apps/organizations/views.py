from django.shortcuts import render
from django.views.generic import View
from apps.organizations.models import CourseOrg, City, Teacher
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class OrgView(View):
    def get(self, request, *args, **kwargs):
        """
        展示授课机构列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        #  获取类别，然后根据类别查询机构
        category = request.GET.get("ct", "")
        #  将接口返回前台进行验证和级联查询
        ct = category
        if category:
            all_orgs = all_orgs.filter(category=category)

        #  获取城市id，根据城市id查询机构
        city_id = request.GET.get("city", "")
        #  将接口返回前台进行验证和级联查询
        try:
            city = int(city_id)
        except Exception as e:
            city = None

        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        #  在接口中获取排序规则
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        #  获取查询后的机构总数
        org_nums = all_orgs.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, per_page=5, request=request)  # 每页显示5个

        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'org_nums': org_nums,
            'all_citys': all_citys,
            'category': category,
            'ct': ct,
            'city_id': city,
            'title': '授课机构',
            'sort': sort,
            'hot_orgs': hot_orgs,
        })


class AddAsk(View):
    '''
    处理用户咨询模块
    '''
    def post(self, request, *args, **kwargs):
        pass