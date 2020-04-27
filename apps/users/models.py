from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract = True  # 作为基类，抽象，不生成表


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=50, verbose_name='gender', choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    icon = models.ImageField(verbose_name='用户头像', upload_to='icon/%Y/%m/%d/', default='default.jpg')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name+'555'

    # def unread_numbers(self):
    #     """
    #     未读消息数量
    #     :return:
    #     """
    #     return self.usermessage_set.filter(has_read=False).count()

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
