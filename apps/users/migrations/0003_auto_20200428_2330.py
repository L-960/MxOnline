# Generated by Django 2.2 on 2020-04-28 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200427_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='icon',
            field=models.ImageField(default='default.jpg', upload_to='users/icon/%Y/%m/%d/', verbose_name='用户头像'),
        ),
    ]
