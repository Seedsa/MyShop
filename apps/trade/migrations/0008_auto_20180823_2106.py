# Generated by Django 2.0.7 on 2018-08-23 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20180823_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='good',
            new_name='goods',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='goods_num',
            new_name='nums',
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 122178), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 121176), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 23, 21, 6, 16, 121176), verbose_name='添加时间'),
        ),
    ]
