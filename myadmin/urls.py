#后台管理子路由文件
from django.urls import path
from myadmin.views import index
from myadmin.views import user
from myadmin.views import shop
from myadmin.views import answers
from myadmin.views import resource

urlpatterns = [
    path('', index.index, name="myadmin_index"), #后台首页

    #后台管理员登录、退出路由
    path('login', index.login, name="myadmin_login"), #加载登录表单
    path('dologin', index.dologin, name="myadmin_dologin"), #执行登录
    path('logout', index.logout, name="myadmin_logout"), #退出
    path('verify', index.verify, name="myadmin_verify"), #输出验证码

    #用户管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"), #浏览
    path('user/add', user.add, name="myadmin_user_add"), #添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"), #执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"), #执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"), #加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"), #执行编辑

    #问题信息管理路由
    path('shop/<int:pIndex>', shop.index, name="myadmin_shop_index"), #浏览
    path('shop/add', shop.add, name="myadmin_shop_add"), #添加表单
    path('shop/insert', shop.insert, name="myadmin_shop_insert"), #执行添加
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_delete"), #执行删除
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"), #加载编辑表单
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"), #执行编辑

    # 回答信息管理路由
    path('answers/<int:pid>/<int:pIndex>', answers.index, name="myadmin_answers_index"),  # 浏览
    path('answers/add/<int:pid>', answers.add, name="myadmin_answers_add"),  # 添加表单
    path('answers/insert/<int:pid>', answers.insert, name="myadmin_answers_insert"),  # 执行添加
    path('answers/del/<int:sid>', answers.delete, name="myadmin_answers_delete"),  # 执行删除
    path('answers/edit/<int:sid>', answers.edit, name="myadmin_answers_edit"),  # 加载编辑表单
    path('answers/update/<int:sid>', answers.update, name="myadmin_answers_update"),  # 执行编辑

    path('resource/<int:pIndex>', resource.index, name="myadmin_resource_index"), #浏览

]