#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel

class User(AbstractUser, BaseModel):
    """用户"""
    #remark = models.CharField(max_length=256, verbose_name="备注")
    class Meta:
        #指定表的名称
        db_table = "mem_users"
