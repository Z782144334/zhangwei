# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models


class DyModels(models.Model):  # 创建数据库和写入读取
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    link = models.CharField(max_length=100, null=False)


