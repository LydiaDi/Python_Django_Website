from django.shortcuts import render

def index(request ,pIndex=1):
    '''执行信息编辑'''
    context = {'info':"等待扩展！"}
    return render(request,"myadmin/info.html",context)