# Generated by Django 2.0.7 on 2018-08-23 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0007_auto_20180823_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 124201), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 123181), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 123181), verbose_name='添加时间'),
        ),
    ]
