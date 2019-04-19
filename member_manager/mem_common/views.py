from django.shortcuts import render, redirect
from django.views.generic import View
import re
from mem_list.models import Member,Apply
from mem_user.models import User
from django.http import Http404
from django.contrib.auth.decorators import login_required
from mem_list.views import get_member
import os
import os.path

@login_required
def get_index(request):
    user = request.user
    members = Member.objects.filter(mem_host_owner_id=user.id)
    context = {
        'user' : user,
        'members' : members,
            }
    response = render(request, 'common/index.html',context)
    return response

@login_required
def get_host(request):
    member_list = get_member(request)
    context = { 
        'member_list' : member_list,
            }   
    response = render(request, 'common/host_list.html', context)
    return response

@login_required
def apply_get(request, host_id):
    try:
        host = Member.objects.get(pk=host_id)
    except:
        return redirect('/mem_common/host')
    context = {
            'host' :  host  
            }
    print(host.id)
    response = render(request, 'common/apply_detail.html', context )
    return response



@login_required
def apply_hand(request):
    user = request.user    
    form = request.POST
    host_id = form.get('host_id')
    username = form.get('username')
    remark  = form.get('remark')
    user_id = user.id
    apply_status = '1'
    
    host = Member.objects.get(pk=host_id)
    user = User.objects.get(pk=user_id)
    apply_obj = Apply()
    apply_obj.host_id = host_id
    apply_obj.user_id = user_id
    apply_obj.remark = remark
    apply_obj.apply_status = apply_status
    apply_obj.save()
    
    host.mem_host_status = 3
    user.first_name = username
    host.save()
    user.save()
    return redirect("/mem_common/apply_list")


@login_required
def apply_cancel(request, id):
    user = request.user    
    try:
        apply = Apply.objects.get(pk=id)
        host = apply.host
    except:
        return redirect('/mem_common/host')
    host.mem_host_status = 1
    apply.apply_status = 4
    apply.save();    
    host.save()
    return redirect("/mem_common/apply_list")


@login_required
def apply_list(request):
    user = request.user
    apply_list = Apply.objects.filter(user_id = user.id)
    context = {
        "apply_list" : apply_list
    }
    response = render(request, "common/apply_list.html", context)
    return response


@login_required
def get_edit(request):
    user = request.user
    context = {
        "user" : user
    }
    response = render(request, 'common/user_edit.html', context)
    return response



@login_required
def hand_user_edit(request):
    form_data = request.POST
    user_id = form_data.get("user_id")
    try:
        user = User.objects.get(pk=user_id)
    except:
        return redirect('/mem_common/index')
    first_name = form_data.get("first_name")
    username = form_data.get("username")
    password = form_data.get("password")
    confirm_password = form_data.get("confirm_password")
    email = form_data.get("email")
    if(first_name):
        user.first_name = first_name
    if(username):
        user.username = username
    print("密码:%s;重复密码%s",(password, confirm_password))
    if all([password, confirm_password]):
        print("密码:%s;重复密码%s",(password, confirm_password))
        if(password != confirm_password):
            print("密码不一样")
            return redirect("/mem_common/get_edit")
        else:
            user.set_password(password)
    print("密码一样")
    if(email):
        user.email = email
    user.save()                                                                                                                                         
    return redirect('/mem_common/index')



#dir tree
def cover_rate(path, node):
    files = ["updown.png", "snow.png","amber.png","emerald.png","glass.png","ruby.png","gcov.css"]
    global rsp_html
    global file_html
    global div_html
    if(node == root):
        rsp_html += """<div class="foder"> <ul class="ful"> <li>"""
        rsp_html += div_html.format('id1','id2',root)
        rsp_html += """<ul class="ful none" id="id3">"""
    for item in os.listdir(path):
        new_path = path + '/' + item
        if os.path.isdir(new_path):
            print("is dir")
            rsp_html += """<li>"""
            rsp_html += div_html.format('','',item)
            rsp_html += """<ul class="ful none" id="id3">"""
            cover_rate(new_path,item)
            rsp_html += """</ul>"""
            rsp_html += """</li>"""
        else:
            if item in files:
                continue
            rsp_html += """<li>"""
            rsp_html +=  file_html.format('/' + path + '/' + item, item)
            rsp_html += """</li>""" 


rsp_html = ""

file_html = """<div class="fla"><span class="close "></span> <span class="pack "></span> <a class="ftext" href="{}" target="_blank">{}</a></div>"""
div_html = """<div class="fla"><span class="open btn_1" id="{}"></span> <span class="pack btn_1"id="{}"></span> <span class="ftext">{}</span></div>"""
root = "uniq_memdb_sp"

#product rsp_html
def product_rsp():
    path = "static/uniq_memdb_sp/uniq_memdb_sp"
    node = "uniq_memdb_sp"
    cover_rate(path, node)
    global rsp_html
    rsp_html += """</li></ul></li></ul>"""
product_rsp()

from django.utils.safestring import mark_safe
def menu_tree(request):
    global rsp_html
    rsp_html = mark_safe(rsp_html)
    context = { 
        "rsp_html" : rsp_html
    }   
    response = render(request, 'cover_rate/uniqsvr.html', context)
    return response









