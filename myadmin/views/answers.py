# xxx信息管理的视图文件
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import bPub
from myadmin.models import bAns
from datetime import datetime
from django.db.models import Q


def index(request,pid=0, pIndex=1):
    '''浏览信息'''
    pid2=pid
    smod = bAns.objects
    slist = smod.filter(pub_question_id__exact=pid)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(Q(content__contains=kw) | Q(ans_user__contains=kw))
        mywhere.append('keyword=' + kw)
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        slist = slist.filter(status=status)
        mywhere.append("status=" + status)

    slist = slist.order_by("id")  # 对id排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 10)  # 以每页10条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {"shoplist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere,'pid':pid2}
    return render(request, "myadmin/answers/index.html", context)


def add(request,pid=0):
    '''加载信息添加表单'''
    ob = bPub.objects.get(id=pid)
    pid2 = pid
    context = {'pid': pid2}
    return render(request, "myadmin/answers/add.html",context)


def insert(request,pid=0):
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

        # 实例化model，封装信息，并执行添加操作
        op = bPub.objects.get(id=pid)

        ob = bAns()
        ob.content = request.POST['content']
        ob.status = 1
        ob.pub_question_id=op.id
        ob.pub_user_id = op.pub_user_id
        ob.pub_user =op.pub_user
        ob.ans_user_id = request.session['adminuser']['id']
        ob.ans_user = request.session['adminuser']['username']
        ob.ans_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myadmin/info.html", context)


def delete(request, sid=0):
    '''执行信息删除'''
    try:
        ob = bAns.objects.get(id=sid)
        ob.status = 0
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "删除成功！"}
    except Exception as err:
        print(err)
        context = {'info': "删除失败！"}
    return render(request, "myadmin/info.html", context)


def edit(request, sid=0):
    '''加载信息编辑表单'''
    try:
        ob = bAns.objects.get(id=sid)
        context = {'ans': ob}
        return render(request, "myadmin/answers/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)


def update(request, sid):
    '''执行信息编辑'''
    try:
        ob = bAns.objects.get(id=sid)
        ob.content = request.POST['content']
        ob.status = request.POST['status']
        ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)