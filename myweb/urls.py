#前台端子路由文件
from django.urls import path,include
from myweb.views import index,example,question,judge,crawler

urlpatterns = [
    #没有登陆的用户所看到的界面
    path('base', index.indexA, name="indexA"),#之前的注释：与web_index区别:只是用于引导到web_index路由的“工具”路由！
    path('base/<int:pIndex>', index.indexA, name="indexA"),
    path('detailA/<int:pubID>', index.detailA, name="web_detailA"),
    path('detailA/<int:pubID>/<int:pIndex>', index.detailA, name="web_detailA"),
    path('hotA', index.hotA, name="web_hotA"),
    #path('login', index.login, name="web_login"), #加载登录表单

#path('carwler', crawler.carwler, name="web_carwler"),#
path('', crawler.carwler, name="web_carwler"),#
path('carwler_1', crawler.carwler_1, name="web_carwler_1"),#
path('carwler_2', crawler.carwler_2, name="web_carwler_2"),#本来有用Python解析数据的想法  后来发现还是得Javascript
path('blank', crawler.blank, name="web_blank"),#

    #实例教程模块的路由
    path('exA', example.exA, name="web_exA"),#这是一个列表页，会分为这个没有登陆就可以看到的页面和另一个登陆才可以看到的页面，另外三个详细内容相关页面，没登陆和登陆者看到的是一样的

    path('ex1', example.ex1, name="web_ex1"),
    path('ex1_down', example.ex1_down, name="web_ex1_down"),
    path('ex1_1', example.ex1_1, name="web_ex1_1"),#执行python代码
    path('ex1_2', example.ex1_2, name="web_ex1_2"),#执行python代码
    path('ex1_3', example.ex1_3, name="web_ex1_3"),#执行python代码

    path('ex2', example.ex2, name="web_ex2"),
    path('ex2_down', example.ex2_down, name="web_ex2_down"),
    path('ex2_1', example.ex2_1, name="web_ex2_1"),
path('ex2_2', example.ex2_2, name="web_ex2_2"),
path('ex2_3', example.ex2_3, name="web_ex2_3"),

    path('ex3', example.ex3, name="web_ex3"),
path('ex3_down', example.ex3_down, name="web_ex3_down"),
path('ex3_down2', example.ex3_down2, name="web_ex3_down2"),

#进行判断从而知道该转向哪个页面
    path('judge1', judge.judge1, name="judge1"),#执行python代码
    path('judge2', judge.judge2, name="judge2"),#执行python代码
    path('judge3', judge.judge3, name="judge3"),#执行python代码
path('judge4', judge.judge4, name="judge4"),#执行python代码
path('judge5', judge.judge5, name="judge5"),

    #前端登陆退出的路由
    path('login', index.login, name="web_login"), #加载登录表单
    path('login2', index.login2, name="web_login2"), #加载登录表单
    # path('dologin', index.dologin, name="web_dologin"), #执行登录
    path('dologin2', index.dologin2, name="web_dologin2"), #执行登录
    path('logout', index.logout, name="web_logout"), #退出
    # path('verify', index.verify, name="web_verify"), #输出验证码
    path('register', index.register, name="web_register"), #加载注册表单
    path('doregister', index.doregister, name="web_doregister"), #执行注册





    #为url路由添加请求前缀web/,凡是带此前缀的url地址必须登录后才可访问
    path("web/",include([
path('carwler_1_2', crawler.carwler_1_2, name="web_carwler_1_2"),
path('carwler', crawler.carwler2, name="web_carwler2"),
path('ex', example.ex, name="web_ex"),
#path('ex/<int:pIndex>', example.ex, name="web_ex"),
    path('', index.webIndex, name="web_index"), #前台首页
    path('<int:pIndex>', index.webIndex, name="web_index"), #前台首页
    # path('detail', index.detail, name="web_detail"),
    path('detail/<int:pubID>', index.detail, name="web_detail"),
    path('detail/<int:pubID>/<int:pIndex>', index.detail, name="web_detail"),
    path('hot', index.hot, name="web_hot"),
    #发布问题路由
    path('pub/add', question.add, name="web_question_add"), #添加表单
    path('pub/insert', question.insert, name="web_question_insert"), #执行添加
path('pub/insertEx', question.insertEx, name="web_question_insertEx"), #执行实例教程模块种的添加
    #回答问题路由
    path('pub/insertAns/<int:pid>', question.insertAns, name="web_question_insertAns"),  # 执行添加
    # path('cart/add/<str:pid>', cart.add, name="web_cart_add"), #购物车添加
    # path('cart/delete/<str:pid>', cart.delete, name="web_cart_delete"), #购物车删除
    # path('cart/clear', cart.clear, name="web_cart_clear"), #购物车清空
    # path('cart/change', cart.change, name="web_cart_change"), #购物车更改
    #
    # #订单处理路由
    # path('orders/<int:pIndex>', orders.index, name="web_orders_index"), #订单浏览
    # path('orders/insert', orders.insert, name="web_orders_insert"), #执行订单添加
    # path('orders/detail', orders.detail, name="web_orders_detail"), #订单详情
    # path('orders/status', orders.status, name="web_orders_status"), #修改订单状态
    ]))
]
