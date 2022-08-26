from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from myadmin.models import bUser,bPub,bAns
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
import random

# Create your views here.
def indexA(request,pIndex=1):
    '''浏览信息'''
    # 方便判断用户是否登录
    request.session['webuserIsLogin'] = 0;

    smod = bPub.objects
    slist = smod
    # slist = smod.filter(status__lt=1)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(Q(pub_user__contains=kw) | Q(title__contains=kw))
        mywhere.append('keyword=' + kw)

    slist = slist.order_by("-pub_time")  # 按时间排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 6)  # 以每页6条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {"shoplist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myweb/indexA.html", context)

def webIndex(request,pIndex=1):
    '''项目前台首页'''
    #return render(request,"myweb/index.html")
    '''浏览信息'''
    smod = bPub.objects
    slist = smod
    # slist = smod.filter(status__lt=1)
    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(Q(pub_user__contains=kw) | Q(title__contains=kw))
        mywhere.append('keyword=' + kw)

    slist = slist.order_by("-pub_time")  # 按时间排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 6)  # 以每页6条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {"shoplist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myweb/index.html", context)

def detail(request,pubID,pIndex=1):
    '''浏览对应问题的回答信息'''
    #1、将该问题查找出来进行显示：
    question= bPub.objects.get(id=pubID)

    smod = bAns.objects
    slist = smod.filter(pub_question_id__exact=pubID)

    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(ans_user__contains=kw)
        mywhere.append('keyword=' + kw)

    slist = slist.order_by("-ans_time")  # 按时间排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 6)  # 以每页6条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {'question':question,"shoplist": list2, 'plist': plist,'pubID':pubID, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myweb/detail.html", context)

def detailA(request,pubID,pIndex=1):
    '''浏览对应问题的回答信息'''
    #1、将该问题查找出来进行显示：
    question= bPub.objects.get(id=pubID)

    smod = bAns.objects
    slist = smod.filter(pub_question_id__exact=pubID)

    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(ans_user__contains=kw)
        mywhere.append('keyword=' + kw)

    slist = slist.order_by("-ans_time")  # 按时间排序
    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(slist, 6)  # 以每页6条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息
    context = {'question':question,"shoplist": list2, 'plist': plist,'pubID':pubID, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myweb/detailA.html", context)

def hot(request):
    smod = bPub.objects

    slist = bPub.objects
    # #slist = smod.filter(status__lt=1)
    # for vo in slist:
    #     vo.help=bAns.objects.filter(pub_question_id=vo.id).count()
    #筛选出回答数目为前8的问题
    slist = slist.order_by("-pub_user_id")  # 按回答数目排序
    slist = slist.all()[0:7]

    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(Q(pub_user__contains=kw) | Q(title__contains=kw))
        mywhere.append('keyword=' + kw)

    context = {"shoplist": slist, 'mywhere': mywhere}
    return render(request, "myweb/index2.html", context)

def hotA(request):
    smod = bPub.objects

    slist = bPub.objects
    # #slist = smod.filter(status__lt=1)
    # for vo in slist:
    #     vo.help=bAns.objects.filter(pub_question_id=vo.id).count()
    #筛选出回答数目为前8的问题
    slist = slist.order_by("-pub_user_id")  # 按回答数目排序
    slist = slist.all()[0:7]

    mywhere = []
    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        slist = smod.filter(Q(pub_user__contains=kw) | Q(title__contains=kw))
        mywhere.append('keyword=' + kw)

    context = {"shoplist": slist, 'mywhere': mywhere}
    return render(request, "myweb/indexA2.html", context)

def login(request):
    '''加载登录页面'''
    return render(request,"myweb/login.html")
def login2(request):
    '''加载登录页面'''
    return render(request,"myweb/login2.html")
def register(request):
    '''加载注册页面'''
    return render(request,"myweb/register.html")

def dologin(request):
    '''执行登录'''
    #验证判断
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        # return redirect(reverse('web_login')+"?typeinfo=1")
        context = {'info':'验证码错误！'}
        return render(request,"myweb/login2.html",context)
    try:
        #根据登录账号获取用户信息
        user = bUser.objects.get(username=request.POST['username'])
        # 校验当前用户状态是否是管理员
        if user.status != 9:
            #获取密码并md5
            import hashlib
            md5 = hashlib.md5()
            n = user.password_salt
            s = request.POST['pass']+str(n)
            md5.update(s.encode('utf-8'))
            # 校验密码是否正确
            if user.password_hash == md5.hexdigest():
                # 将当前登录成功用户信息以adminuser这个key放入到session中
                request.session['webuser']=user.toDict()
                #跳转首页
                return redirect(reverse('web_index'))
            else:
                context={"info":"登录密码错误！"}
                return redirect(reverse('web_login')+"?typeinfo=2",context)
        else:
            #context={"info":"此用户在数据库中但是已注销！"}
            return redirect(reverse('web_login')+"?typeinfo=3")
    except Exception as err:
        print(err)
        #此用户不存在
        #context={"info":"登录账号不存在！"}
        return redirect(reverse('web_login')+"?typeinfo=4")
    #return render(request,"web/login.html",context)
def dologin2(request):
    '''执行登录'''
    #验证判断
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        #return redirect(reverse('web_login2')+"?typeinfo=1")
        context = {'info':'验证码错误！'}
        return render(request,"myweb/login2.html",context)
    try:
        #根据登录账号获取用户信息
        user = bUser.objects.get(username=request.POST['username'])
        # 校验当前用户状态是存在
        if user.status != 9:
            #获取密码并md5
            import hashlib
            md5 = hashlib.md5()
            n = user.password_salt
            s = request.POST['pass']+str(n)
            md5.update(s.encode('utf-8'))
            # 校验密码是否正确
            if user.password_hash == md5.hexdigest():

                #计算总共发布了几个问题
                pubCount = bPub.objects.filter(pub_user_id=user.id).count()
                #print(pubCount)
                request.session['webuserAllPub'] = pubCount
                # 计算总共回答了几个问题
                ansCount= bAns.objects.filter(ans_user_id=user.id).count()
                #print(ansCount)
                request.session['webuserAllAns'] = ansCount

                #方便判断用户是否登录
                request.session['webuserIsLogin'] = 1

                # 将当前登录成功用户信息以adminuser这个key放入到session中
                request.session['webuser'] = user.toDict()

                #跳转首页
                return redirect(reverse('web_index'))
            else:
                context={"info":"登录密码错误！"}
                #return redirect(reverse('web_login2')+"?typeinfo=2",context)
                return render(request, "myweb/login2.html", context)
        else:
            #此用户在数据库中但是已注销
            context={"info":"已注销,请重新注册"}
            #return redirect(reverse('web_login2')+"?typeinfo=3")
            return render(request, "myweb/login2.html", context)
    except Exception as err:
        print(err)
        #此用户不存在
        context={"info":"此账号不存在，请注册"}
        #return redirect(reverse('web_login2')+"?typeinfo=4")
        return render(request, "myweb/login2.html", context)
def doregister(request):
    '''执行注册'''
    #验证判断
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        #return redirect(reverse('web_login2')+"?typeinfo=1")
        context = {'info':'验证码错误！'}
        return render(request,"myweb/register.html",context)
    try:
        count=bUser.objects.filter(username=request.POST['username']).count()
        if count==1:
            context = {'info': '此用户名已被使用！'}
            return render(request, "myweb/register.html", context)
        else:
            pwd1=request.POST['pass']
            pwd2=request.POST['pass2']
            if pwd1!=pwd2:
                context = {'info': '两次输入密码不一致！'}
                return render(request, "myweb/register.html", context)
            else:
                ob=bUser()
                ob.username = request.POST['username']
                # if(request.POST['phone']==''):
                #     ob.phone = "未绑定";
                #
                # else:
                #     ob.phone = request.POST['phone']

                ob.status = 1
                ob.create_time = datetime.now()
                ob.update_time = datetime.now()
                ob.email="未绑定";
                ob.phone = "未绑定";
                # ob.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # ob.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # 将密码做md5处理
                import hashlib, random
                md5 = hashlib.md5()
                n = random.randint(100000, 999999)
                s = request.POST['pass'] + str(n)  # 从表单中获取密码并添加干扰值
                md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
                ob.password_hash = md5.hexdigest()  # 获取md5值
                ob.password_salt = n
                ob.save()

                # 计算总共发布了几个问题
                pubCount = bPub.objects.filter(pub_user_id=ob.id).count()
                # print(pubCount)
                request.session['webuserAllPub'] = pubCount
                # 计算总共回答了几个问题
                ansCount = bAns.objects.filter(ans_user_id=ob.id).count()
                # print(ansCount)

                request.session['webuserAllAns'] = ansCount
                request.session['webuser'] = ob.toDict()
                context = {'info': "添加成功！"}
                # 跳转首页
                return redirect(reverse('web_index'))
    except Exception as err:
        print(err)
        context={"info":"未注册成功，请稍后再试"}
        return render(request,"myweb/register.html",context)
def logout(request):
    '''执行退出'''
    del request.session['webuser']
    del request.session['webuserAllPub']
    del request.session['webuserAllAns']
    # 方便判断用户是否登录
    request.session['webuserIsLogin'] = 0;
    return redirect(reverse('web_login2'))

def verify(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    #str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/arial.ttf', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')