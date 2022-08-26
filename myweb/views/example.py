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

def ex3_test(request):
    import requests
    import re
    import json
    import pymysql
    import time

    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           db="corona")

    cursor = conn.cursor()

    sql = "insert into details values (%s,%s,%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sql,[2,time.strftime("%Y-%m-%d"),"2","2",2,2,2])#time.strftime("%Y-%m-%d")用不了，不知道为啥
    # 因为上面的time.strftime用不了，所以我将update_time的数据的数据类型由datetime变成了varchar
    cursor.execute(sql, [2, "2022-1-1", "2", "2", 2, 2, 2, 2])
    conn.commit()  # 提交事务
    # res=cursor.fetchall()
    # print(res)

    cursor.close()
    conn.close()
    return render(request,"myweb/example/example1.html")

def exA(request):
    # login=int(request.session['webuserIsLogin'])
    # if(login):
    #     isLogin = request.session['webuserIsLogin']
    #     print(isLogin)
    #     context = {"isLogin": isLogin}
    #     return render(request, "myweb/example/exampleListA.html", context)
    # else:
    #     print(login)
    #     return render(request, "myweb/example/exampleListA.html")

    #因为显示“登录/注册”还是“退出”的判断是直接根据session值进行判断的，所以跟不需要用上面的写法直接写下面这一句话，渲染模板即可
    return render(request, "myweb/example/exampleListA.html")

def ex(request):
    return render(request, "myweb/example/exampleList.html")

#ex1
def ex1(request):
    # return render(request,"myweb/example/example1.html")

    login = int(request.session['webuserIsLogin'])
    if (login):
        isLogin = request.session['webuserIsLogin']
        print(isLogin)
        context = {"isLogin": isLogin}
        return render(request, "myweb/example/example1.html", context)
    else:
        print(login)
        context = {"isLogin": 0}
        return render(request, "myweb/example/example1.html", context)

def ex1_down(request):
    file = open('static/myweb/files/dangdangTop500.py', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="dangdangTop500.py"'
    return response

def ex1_1(request):

    #可以实现的代码
    # import urllib.request
    # url="https://www.baidu.com"
    # res=urllib.request.urlopen(url)
    # print(res.info)
    # print(res.getcode())
    # print(res.geturl())
    # context = {"a": res.getcode()}
    # return render(request, "myweb/example/example1.html",context)
    #
    #下面这种传值方式不可以实现，只能用上面呢种传值方式
    # a=res.getcode()
    # return render(request, "myweb/example/example1.html", a)

    import requests
    url=request.POST['href']
    context = {"a": requests.get(url)}
    return render(request, "myweb/example/example1.html", context)

def ex1_2(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    context = {"b": response.status_code}
    return render(request, "myweb/example/example1.html", context)

def ex1_3(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    response.encoding = "utf-8"
    context = {"c": response.text}
    return render(request, "myweb/example/example1.html", context)

#ex2
def get_conn():
    #创建连接
    conn=pymysql.connect(host="localhost",
                  user="root",
                  password="123456",
                  db="osdb")
    #创建游标
    cursor=conn.cursor()#执行完毕返回的结果集默认以元组显示
    return conn,cursor
def close_conn(conn,cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
def query(sql,*args):
    conn,cursor=get_conn()
    cursor.execute(sql,args)
    res=cursor.fetchall()
    close_conn(conn,cursor)
    return res

def ex2(request):
    '''浏览信息'''
    list = details.objects
    list = list.order_by("id")  # 对id排序
    context = {"list": list}
    return render(request, "myweb/example/example2.html", context)

def get_tencent_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    r = requests.get(url)
    res = json.loads(r.text)  # json字符串转字典
    data_all = json.loads(res['data'])

    details = []  # 当日详细数据
    update_time = data_all["lastUpdateTime"]
    data_country = data_all["areaTree"]  # list 25个国家
    data_province = data_country[0]["children"]  # 中国各省
    for pro_infos in data_province:
        province = pro_infos["name"]  # 省名
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]
            confirm = city_infos["total"]["confirm"]
            confirm_add = city_infos["today"]["confirm"]
            heal = city_infos["total"]["heal"]
            dead = city_infos["total"]["dead"]
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return details
def update_details():
    conn=None
    cursor=None
    try:
        li=get_tencent_data()
        conn,cursor=get_conn()
        sql="insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values (%s,%s,%s,%s,%s,%s,%s)"
        sql_query="select %s=(select update_time from details order by id desc limit 1)" #对于当前最大时间戳
        cursor.execute(sql_query,li[0][0])  #为什么这里填li[0][0]正确，而填写li[0]就错误呢？我感觉应该写li[0]？
        if not cursor.fetchone()[0]:  #必须加上"[0]"
            print(f"{time.asctime()}开始更新最新数据")
            for item in li:
                cursor.execute(sql,item)  #这一句中逗号后面具体写什么，要看便历的item所对应的数据是什么数据类型，
                #假如是字典类型就要用下面一句话这种形式。
                #cursor.execute(sql, [item["range"],item["image"],item["title"],item["recommend"],item["author"],item["times"],item["price"]])
            conn.commit()
            print(f"{time.asctime()}更新最新数据完毕")
        else:
            print(f"{time.asctime()}已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)
def ex2_1(request):
    '''浏览信息'''
    update_details()
    list = details.objects
    list = list.order_by("id")  # 对id排序
    context = {"list": list}
    return render(request, "myweb/example/example2.html", context)

def ex2_2(request):
    import requests
    url = request.POST['href']
    response=requests.get(url)
    response.encoding = "utf-8"
    res=json.loads(response.text)
    context = {"a": response.text,"b":res,"c":json.loads(res['data'])}
    return render(request, "myweb/example/example2.html", context)

def ex2_3(request):
    details=get_tencent_data()
    context = {"d": details}
    return render(request, "myweb/example/example2.html", context)

def ex2_down(request):
    file = open('static/myweb/files/TecentCovidData.py', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="TecentCovidData.py"'
    return response

#ex3
def ex3(request):
    import sqlite3
    import json
    sql = "SELECT city,confirm_add FROM (SELECT city,confirm_add FROM details where update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1 ) and province not in('北京','上海','天津','重庆','香港','台湾') union all SELECT province as city,SUM(confirm_add) as confirm_add from details where update_time=(SELECT update_time FROM details ORDER BY update_time DESC LIMIT 1 ) and province in ('北京','上海','天津','重庆')  GROUP BY province) as a ORDER BY confirm_add DESC LIMIT 5"
    res=query(sql)
    city=[]
    confirm=[]
    for k,v in res:
        city.append(k)
        confirm.append(int(v))
    context = {"city":city,"confirm":confirm}
    print(context)
    return render(request,"myweb/example/example3.html",context)

def ex3_down(request):
    file = open('static/myweb/files/echarts.js', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="echarts.js"'
    return response
def ex3_down2(request):
    file = open('static/myweb/files/复现示例.html', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="复现示例.html"'
    return response
