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

def carwler(request):
    request.session['webuserIsLogin'] = 0;
    return render(request, "myweb/crawler/process.html")
def carwler2(request):
    return render(request, "myweb/crawler/process2.html")

def carwler_1(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    response.encoding = "utf-8" #注释之后可以进行当当网数据爬取
    context = {"a": response.text}
    return render(request, "myweb/crawler/process.html", context)
    #return render(request, "myweb/crawler/blank.html", context)

def carwler_1_2(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    response.encoding = "utf-8"
    context = {"a": response.text}
    return render(request, "myweb/crawler/process2.html", context)

def carwler_2(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    #response.encoding = "utf-8"

    context = {"b": response.text}
    return render(request, "myweb/crawler/process.html", context)
    #return render(request, "myweb/crawler/blank.html", context)

def blank(request):
    return render(request, "myweb/crawler/blank.html")
