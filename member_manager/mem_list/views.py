from django.shortcuts import render, redirect
from django.views.generic import View
import re
from .models import Member, Apply
from django.http import Http404
from django.contrib.auth.decorators import login_required
from mem_user.models import User
from utils.views import is_super
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse

@login_required
def get_member(request):
    members = Member.objects.filter(isDelete=False)
    return members

#增加会员页面
@is_super
@login_required
def get_add(request):
    return render(request, 'add_member.html')
    

#增加主机表单提交
@csrf_exempt
@is_super
@login_required
def add_list(request):
    print("enter view")
    dict1 = request.POST
    mem_ip = dict1.get('mem_ip')
    mem_login_name = dict1.get('mem_login_name')
    mem_login_pwd = dict1.get('mem_login_pwd')
    mem_remark = dict1.get('mem_remark')
    context = { 
        'rsp_code' : -1, 
        'rsp_msg':'',
    }   
    if not all([mem_ip, mem_login_name, mem_login_pwd]):
        print("w数据不完整")
        context["rsp_msg"] = "数据不完整，请重新输入！"
        return JsonResponse(context)
    member = Member.objects.filter(mem_ip=mem_ip,mem_login_name=mem_login_name)
    if(member):
        print("主机名已经存在")
        context["rsp_msg"] = "该主机用户名已存在，请重新输入！"
        return JsonResponse(context)
    member = Member()
    member.mem_host_num = Member.objects.filter(mem_ip=mem_ip).count() + 1
    member.mem_ip = mem_ip
    member.mem_login_name = mem_login_name
    member.mem_login_pwd = mem_login_pwd
    member.mem_remark = mem_remark
    member.save()
    print("添加成功")	
    context["rsp_code"] = 0
    return JsonResponse(context)
@is_super
@login_required
def member_list(request):
    member_list = get_member(request)
    context = {
        'member_list' : member_list
            }
    response = render(request, 'tables.html', context)
    return response


@is_super
@login_required
def member_edit(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
    except:
        return render(request, 'login.html')
    context = {
            'member' : member
            }
    response = render(request, 'edit_member.html', context)
    return response

@is_super
@login_required
def member_edit_hand(request):
    dict1 = request.POST
    mem_id = dict1.get('mem_id')
    mem_name = dict1.get('mem_name')
    mem_ip = dict1.get('mem_ip')
    mem_login_name = dict1.get('mem_login_name')
    mem_login_pwd = dict1.get('mem_login_pwd')
    mem_remark = dict1.get('mem_remark')

    try:
        member = Member.objects.get(pk=mem_id)
    except:
        return Http404()
    member.mem_name = mem_name
    member.mem_ip = mem_ip
    member.mem_login_name = mem_login_name
    member.mem_login_pwd = mem_login_pwd
    member.mem_remark = mem_remark
    member.save()
    return redirect('/mem_list/member_list')    

@is_super
@login_required
def member_delete(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
    except:
        return render(request, 'login.html')
    member.isDelete = True
    member.save()
    return redirect('/mem_list/member_list')

@is_super
@login_required
def get_userlist(request):
    users = User.objects.filter(isDelete=False)
    context = { 
            'users' : users
            }   
    response = render(request, 'user.html', context)
    return response


@is_super
@login_required
def delete_user(request, user_id):
    if user_id == 1:
        return redirect('/mem_list/user_list')
    try:
        user = User.objects.get(pk=user_id)
    except:
        return redirect('/mem_list/user_list')
    user.isDelete = True
    user.save()
    print(user.id)
    return redirect('/mem_list/user_list')



        
@is_super
@login_required
def apply_list(request):
    apply_list = Apply.objects.filter().order_by('-id')
    context = { 
        "apply_list" : apply_list
    }   
    response = render(request, "apply_list.html", context)
    return response

@is_super
@login_required
def apply_pass(request, apply_id):
    try:
        apply_obj = Apply.objects.get(pk=apply_id)
    except:
        return redirect('/mem_list/apply_list')
    apply_obj.apply_status = '2'
    host = apply_obj.host
    user = apply_obj.user
    host.mem_host_owner = user
    host.mem_host_status = '2'
    apply_obj.save()
    host.save()
    mail_body = '尊敬的%s,您申请的主机已经审核通过。请登陆系统查看' % user.first_name
    send_mail('通知信息', '', settings.EMAIL_FROM, [user.email], html_message=mail_body)
    return redirect('/mem_list/apply_list')


@is_super
@login_required
def refuse(request, apply_id):
    context = {
        "apply_id" : apply_id
    }
    response = render(request, 'refuse.html', context)
    return response

@is_super
@login_required
def refuse_hand(request):
    form = request.POST
    apply_id = form.get("apply_id")
    fail_reason = form.get("fail_reason")
    try:
        apply_obj = Apply.objects.get(pk=apply_id)
    except:
        return ("/mem_list/apply_list")
    apply_obj.fail_reason = fail_reason
    apply_obj.apply_status = '3'
    host = apply_obj.host
    host.mem_host_status = '1'
    apply_obj.save()
    host.save()
    return redirect('/mem_list/apply_list')


@login_required
def get_user_edit(request, user_id):
    try:
        user = User.objects.get(pk=user_id)    
    except:
        return redirect('/mem_list/user_list') 
    context = {
        "user" : user
    }
    response = render(request, 'user_edit.html', context)
    return response
    

@login_required
def hand_user_edit(request):
    form_data = request.POST
    user_id = form_data.get("user_id")
    try:
        user = User.objects.get(pk=user_id)
    except:
        return redirect('/mem_list/user_list')
    first_name = form_data.get("first_name")
    username = form_data.get("username")
    password = form_data.get("password")
    confirm_password = form_data.get("confirm_password")
    email = form_data.get("email")
    if(first_name):
        user.first_name = first_name
    if(username):
        user.username = username
    if all([password, confirm_password]):
        if(password != confirm_password):
            return redirect("/mem_list/get_user_edit/"+user_id)
        else:
            user.set_password(password)
    if(email):
        user.email = email
    user.save()
    my_self = request.user
    if(my_self.is_superuser):
        return redirect('/mem_list/user_list')
    else:
        return redirect('/mem_common/index')








