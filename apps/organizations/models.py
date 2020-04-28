from django.db import models

from apps.users.models import BaseModel, UserProfile


class City(BaseModel):
    name = models.CharField(max_length=100, verbose_name="城市")
    desc = models.CharField(max_length=300, verbose_name="描述", default="")

    class Meta:
        verbose_name = "城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    city = models.ForeignKey(City, verbose_name="所属城市", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="机构名称")
    tag = models.CharField(max_length=50, verbose_name="机构标签", default="")
    category = models.CharField(max_length=50, verbose_name="机构类别", default="技术类")
    org = models.CharField(max_length=10, verbose_name="培训机构", choices=(
        ('gr', '个人'), ('gx', '高校')
    ))
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    address = models.CharField(max_length=100, verbose_name="机构地址")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    course_nums = models.IntegerField(verbose_name="课程数", default=0)
    is_auth = models.BooleanField(verbose_name="是否认证", default=False)
    is_goldmedal = models.BooleanField(verbose_name="是否金牌", default=False)
    image = models.ImageField(upload_to='organizations/CourseOrg/img/%Y/%m', verbose_name="logo", max_length=100)

    class Meta:
        verbose_name = "教学机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, verbose_name="用户", null=True, blank=True)
    name = models.CharField(max_length=10, verbose_name="教师名")
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    work_years = models.IntegerField(verbose_name="工作年限（单位月）", default=0)
    company = models.CharField(max_length=50, verbose_name="就职公司", default="")
    company_position = models.CharField(max_length=50, verbose_name="公司职位", default="")
    teaching_trait = models.CharField(max_length=200, verbose_name="教学特点")
    age = models.IntegerField(verbose_name="年龄")
    chick_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    image = models.ImageField(upload_to="organizations/Teacher/icon/%Y/%m", max_length=100)

    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
