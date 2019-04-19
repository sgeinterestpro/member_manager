#coding:utf-8
from django.db import models


# 对于表中都有的字段，在这个类中定义一次，其它类继承于此即可
class BaseModel(models.Model):
    # 数据的创建时间，自动赋值
    add_date = models.DateTimeField(auto_now_add=True)
    # 数据的修改时间，自动赋值
    update_date = models.DateTimeField(auto_now=True)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)
    #这个类不需要生成一张表，需要定义成抽象类
    class Meta:
        abstract=True
