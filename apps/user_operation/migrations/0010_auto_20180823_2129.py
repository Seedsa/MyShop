# Generated by Django 2.0.7 on 2018-08-23 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0009_auto_20180823_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 28, 59, 295695), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 28, 59, 294718), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 28, 59, 294718), verbose_name='添加时间'),
        ),
    ]