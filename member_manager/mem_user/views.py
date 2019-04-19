from django.shortcuts import render, redirect
from django.views.generic import View
import re
from .models import User
from mem_list.models import Member
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def get_register(request):
    return render(request, 'register.html')
    
@csrf_exempt
def post_register(request):
    dict1 = request.POST
    user_name = dict1.get('user_name')
    first_name = dict1.get('first_name')
    email = dict1.get('email')
    pwd = dict1.get('pwd')
    cpwd = dict1.get('cpwd')
   
    context = {
            'rsp_code' : -1,
            'rsp_msg':'',
            }

    print("开始注册")
    #验证数据完整性
    if not all([user_name, email, pwd, cpwd]):
        return JsonResponse(context)
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return JsonResponse(context)
    if pwd != cpwd:
        context["rsp_msg"] = "两次密码输入不一致，请重新输入"
        return JsonResponse(context)
    if User.objects.filter(username=user_name).count() >= 1:
        print("用户名存在")
        context["rsp_msg"] = "用户名已存在，请重新输入！"
        return JsonResponse(context)
    is_superuser = 1
    is_superuser1 = 0
    if User.objects.filter().count() == 0:
        user = User.objects.create_user(user_name, email, pwd)
        user.is_superuser = is_superuser
        user.first_name = first_name
        user.save()
    else:
        user = User.objects.create_user(user_name, email, pwd)
        user.is_superuser = is_superuser1
        user.first_name = first_name
        user.save()
    context["rsp_code"] = 0
    return JsonResponse(context)



def login_get(request):
    username = request.COOKIES.get('username', '')
    context = {
            'username' : username
            }
    return render(request, 'login.html', context)




@csrf_exempt
def login_post(request):
    dict1 = request.POST
    print("enter view")
    username = dict1.get('username')
    pwd = dict1.get('pwd')
    remember = dict1.get('remember')
    context = {
            'rsp_code' : -1,
            'is_super':-1,
            'rsp_msg':'',
            }
    # 2.验证完整性:可以不传递remember
    if not all([username, pwd]):
        context["rsp_msg"] = "数据不完整，请重新输入！"
        return JsonResponse(context)

    user = authenticate(username=username, password=pwd)
    print("数据完整\n")
    if user is None:
        print("用户名不存在\n")
        context["rsp_msg"] = "用户名或密码错误，请重新输入！"
        return JsonResponse(context)
    login(request, user)
    print("登陆成功\n")
    context["rsp_code"] = 0
    if user.is_superuser == 1:
        print("管理员登陆")
        context["is_super"] = 1
        return JsonResponse(context)
    else:
        print("用户登陆")
        context["is_super"] = 0
        return JsonResponse(context)


def user_logout(request):
    logout(request)
    return redirect('/user/login')






