from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import bUser,bPub,bAns,details
from django.shortcuts import render
import pymysql
from django.http import HttpResponse, FileResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import requests
import re
import requests
import pymysql
import time
import json
import traceback  #追踪异常

def judge1(request):
    login=int(request.session['webuserIsLogin'])
    if(login):
        print(login)
        #很神奇，用下面备注是的语句会出错，用不被注释的return语句就正确了？？？！！！
        # return render(request, "myweb/index.html")
        return redirect(reverse('web_index'))
    else:
        print(login)
        # return render(request, "myweb/indexA.html")
        return redirect(reverse('indexA'))

def judge2(request):
    login = int(request.session['webuserIsLogin'])
    if (login):
        print(login)
        return render(request, "myweb/index2.html")
    else:
        print(login)
        return render(request, "myweb/indexA2.html")

def judge3(request):
    login = int(request.session['webuserIsLogin'])
    if (login):
        print(login)
        return redirect(reverse('web_logout'))
    else:
        print(login)
        return render(request, "myweb/login2.html")

def judge4(request):
    login = int(request.session['webuserIsLogin'])
    if (login):
        print(login)
        return render(request, "myweb/example/pubQuestion.html") #发布问题
    else:
        print(login)
        return render(request, "myweb/login2.html")

def judge5(request):
    login = int(request.session['webuserIsLogin'])
    if (login):
        print(login)
        return render(request, "myweb/example/exampleList.html")
    else:
        print(login)
        return render(request, "myweb/example/exampleList.html")