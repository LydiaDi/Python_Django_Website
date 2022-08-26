from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import bUser,bPub,bAns
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import requests
import re
import json

def add(request):
    '''加载信息添加表单'''
    return render(request,"myweb/question/add.html")

def insert(request):
    '''执行信息添加'''
    try:
        # # 店铺封面图片的上传处理
        # myfile = request.FILES.get("cover_pic",None)
        # if not myfile:
        #     return HttpResponse("没有店铺封面上传文件信息")
        # cover_pic = str(time.time())+"."+myfile.name.split('.').pop()
        # destination = open("./static/uploads/shop/"+cover_pic,"wb+")
        # for chunk in myfile.chunks():      # 分块写入文件
        #     destination.write(chunk)
        # destination.close()

        # # 店铺logo图片的上传处理
        # myfile = request.FILES.get("banner_pic",None)
        # if not myfile:
        #     return HttpResponse("没有店铺logo上传文件信息")
        # banner_pic = str(time.time())+"."+myfile.name.split('.').pop()
        # destination = open("./static/uploads/shop/"+banner_pic,"wb+")
        # for chunk in myfile.chunks():      # 分块写入文件
        #     destination.write(chunk)
        # destination.close()

        #实例化model，封装信息，并执行添加操作
        ob = bPub()
        ob.title = request.POST['title']
        ob.content = request.POST['content']
        ob.status = 1
        ob.pub_user_id = request.session['webuser']['id']
        ob.pub_user = request.session['webuser']['username']
        ob.pub_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"添加成功！"}
    except Exception as err:
        print(err)
        context = {'info':"添加失败！"}
    return render(request,"myweb/info.html",context)

def insertAns(request,pid=0):
    try:
        op = bPub.objects.get(id=pid)

        ob = bAns()
        ob.content = request.POST['ans']
        ob.status = 1
        ob.pub_question_id = op.id
        ob.pub_user_id = op.pub_user_id
        ob.pub_user = op.pub_user
        ob.ans_user_id = request.session['webuser']['id']
        ob.ans_user = request.session['webuser']['username']
        ob.ans_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myweb/info.html", context)

def insertEx(request):
    '''执行信息添加'''
    try:
        ob = bPub()
        ob.title = request.POST['title']
        ob.content = request.POST['content']
        ob.status = 1
        ob.pub_user_id = request.session['webuser']['id']
        ob.pub_user = request.session['webuser']['username']
        ob.pub_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"添加成功！"}
    except Exception as err:
        print(err)
        context = {'info':"添加失败！"}
    return render(request,"myweb/example/infoEx.html",context)