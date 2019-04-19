#coding:utf-8  
from django.db import models
from utils.models import BaseModel
from mem_user.models import User

class Member(BaseModel):
    """主机表 """
    HOST_STATUS_CHOICES = (
            (1,"空闲"),
            (2,"被占用"),
            (3,"申请中"),
            )
    mem_ip = models.CharField(max_length=15,  verbose_name="会员IP")
    mem_login_name = models.CharField(max_length=64,  verbose_name="会员登录名")
    mem_login_pwd = models.CharField(max_length=64,  verbose_name="会员登录密码")
    mem_host_num = models.CharField(max_length=64, verbose_name="主机帐号编号")
    mem_host_owner = models.ForeignKey(User, null=True,blank=True, verbose_name="主机使用和者")
    mem_host_status = models.SmallIntegerField(choices=HOST_STATUS_CHOICES, default=1, verbose_name="主机状态")
    mem_remark = models.CharField(max_length=64,  verbose_name="备注")
    class Meta:
        db_table = 'mem_list'
    
class Apply(BaseModel):
    APPLY_STATUS = (
            (1,"申请中"),
            (2,"申请成功"),
            (3,"申请失败"),
            (4,"已撤销"),
            )
    host = models.ForeignKey(Member, verbose_name="主机id")
    user = models.ForeignKey(User, verbose_name="申请者")
    apply_status = models.SmallIntegerField(choices=APPLY_STATUS, default=1, verbose_name="申请状态")
    fail_reason = models.CharField(max_length=64, verbose_name="失败原因") 
    remark = models.CharField(max_length=64, verbose_name="备注")

    class Meat:
        db_table = 'apply_list'












