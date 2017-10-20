# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170830_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='email',
            field=models.EmailField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='captcha',
            name='first',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='captcha',
            name='last',
            field=models.CharField(max_length=25, null=True),
        ),
    ]