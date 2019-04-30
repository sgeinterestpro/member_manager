#coding:utf-8
from django.db import models
from utils.models import BaseModel
from mem_user.models import User
# Create your models here.


class Meetings(BaseModel):
    """会议室表"""
    name = models.CharField(max_length=20, verbose_name="会议室名称")
    address = models.CharField(max_length=30, verbose_name="会议室地址")
    galleryful = models.IntegerField(max_length=50, verbose_name="容纳人数")
    class Meta:
        db_table = "Meetings"


class Reserve(BaseModel):
    """预定信息表"""
#user = models.ForeignKey(User, verbose_name="预定人")
    title = models.CharField(max_length=60,verbose_name="会议内容")
#    meeting = models.ForeignKey(Meetings, verbose_name="会议室")
    start = models.CharField(max_length=60,verbose_name="开始时间")
    end = models.CharField(max_length=60, verbose_name="结束时间")
    timestamp = models.CharField(max_length=60,verbose_name="创建时间")
    room = models.CharField(max_length=100,verbose_name="会议室")
    class Meta:
        db_table = "Reserve"

