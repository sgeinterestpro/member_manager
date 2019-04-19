from django.shortcuts import render, redirect 
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

class LoginRequiredView(View):
    def as_view(cls, **initkwargs):
        view_fun = super().as_view(**initkwargs)
        return login_required(view_fun)


# 当一个类用于多继承时，使用Mixin作为结尾
class LoginRequiredViewMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view_fun = super().as_view(**initkwargs)
        return login_required(view_fun)

def is_super(func):                                                                                        
    def wrapper(request, *argv, **kwargs):
        user = request.user
        if not user.is_superuser:
            return render(request, 'login.html')
        return func(request, *argv, **kwargs)
    return wrapper

#创建celery对象，通过broker指定存储队列的数据库(redis)
#app = Celery('celery_tasks', broker='redis://127.0.0.1:6379/4')
#@app.task
#def send_active_mail(user_email,user_id):
#    #发邮件
#    mail_body = '尊敬的%s,您申请的主机已经审核通过。请登陆系统查看' % user.first_name
#    send_mail('通知信息', '', settings.EMAIL_FROM, [user.email], html_message=mail_body)






