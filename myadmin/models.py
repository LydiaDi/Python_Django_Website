from django.db import models
from datetime import datetime

# Create your models here.
#用户账号信息模型
class bUser(models.Model):
    username = models.CharField(max_length=50)    #用户名
    nickname = models.CharField(max_length=50)    #昵称
    password_hash = models.CharField(max_length=100)#密码
    password_salt = models.CharField(max_length=50)    #密码干扰值
    status = models.IntegerField(default=1)    #状态:1正常/2禁用/6管理员/9注销
    create_time = models.DateTimeField(default=datetime.now)    #创建时间
    update_time = models.DateTimeField(default=datetime.now)    #修改时间
    email = models.CharField(max_length=255)  # 邮箱
    phone = models.CharField(max_length=255)  # 手机号码

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_time':self.create_time.strftime('%Y-%m-%d %H:%M:%S'),'update_time':self.update_time.strftime('%Y-%m-%d %H:%M:%S'),'email':self.email,'phone':self.phone}

    class Meta:
        db_table = "b_user"  # 更改表名

#发布问题信息模型
class bPub(models.Model):
    pub_user_id = models.IntegerField(max_length=50)    #
    pub_user = models.CharField(max_length=255)   #
    title = models.CharField(max_length=255)    #
    content = models.TextField()     #内容
    pub_time = models.DateTimeField(default=datetime.now)    #创建时间
    status = models.IntegerField(default=1)    #状态:1正常/0删除
    update_time= models.DateTimeField(default=datetime.now)
    help =models.IntegerField(max_length=50)

    def toDict(self):
        return {'help':self.help,'id':self.id,'pub_user_id':self.pub_user_id,'pub_user':self.pub_user,'title':self.title,'content':self.content,'pub_time':self.pub_time.strftime('%Y-%m-%d %H:%M:%S'),'status':self.status,'update_time':self.update_time}

    class Meta:
        db_table = "b_pub_question"  # 更改表名

#回答问题信息模型
class bAns(models.Model):
    pub_question_id = models.IntegerField(max_length=50)
    pub_user_id = models.IntegerField(max_length=50)    #
    pub_user = models.CharField(max_length=255)   #
    ans_user_id = models.IntegerField(max_length=50)  #
    ans_user = models.CharField(max_length=255)  #
    content = models.TextField()     #内容
    ans_time = models.DateTimeField(default=datetime.now)    #创建时间
    status = models.IntegerField(default=1)    #状态:1正常/0删除
    update_time= models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id':self.id,'pub_user_id':self.pub_user_id,'pub_user':self.pub_user,'ans_user_id':self.ans_user_id,'ans_user':self.ans_user,'content':self.content,'ans_time':self.ans_time.strftime('%Y-%m-%d %H:%M:%S'),'status':self.status,'update_time':self.update_time}

    class Meta:
        db_table = "b_ans"  # 更改表名

#
class details(models.Model):
    update_time = models.CharField(max_length=255)    #
    province = models.CharField(max_length=255)   #
    city = models.CharField(max_length=255) #
    confirm = models.IntegerField(max_length=50)  #
    confirm_add = models.IntegerField(max_length=50)
    heal= models.IntegerField(max_length=50)
    dead = models.IntegerField(max_length=50)

    def toDict(self):
        return {'update_time':self.update_time,'province':self.province,'city':self.city,'confirm':self.confirm,'confirm_add':self.confirm_add,'heal':self.heal,'dead':self.dead}

    class Meta:
        db_table = "details"  # 更改表名

#员工账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    #员工账号
    nickname = models.CharField(max_length=50)    #昵称
    password_hash = models.CharField(max_length=100)#密码
    password_salt = models.CharField(max_length=50)    #密码干扰值
    status = models.IntegerField(default=1)    #状态:1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间
    email = models.CharField(max_length=255)  # 邮箱
    phone = models.CharField(max_length=255)  # 手机号码

    def toDict(self):
        return {'id':self.id,'username':self.username,'nickname':self.nickname,'password_hash':self.password_hash,'password_salt':self.password_salt,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S'),'email':self.email,'phone':self.phone}

    class Meta:
        db_table = "user"  # 更改表名


#店铺信息模型
class Shop(models.Model):
    name = models.CharField(max_length=255)        #店铺名称
    cover_pic = models.CharField(max_length=255)#封面图片
    banner_pic = models.CharField(max_length=255)#图标Logo
    address = models.CharField(max_length=255)    #店铺地址
    phone = models.CharField(max_length=255)    #联系电话
    status = models.IntegerField(default=1)        #状态:1正常/2暂停/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        shopname = self.name.split("-")
        return {'id':self.id,'name':shopname[0],'shop':shopname[1],'cover_pic':self.cover_pic,'banner_pic':self.banner_pic,'address':self.address,'phone':self.phone,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "shop"  # 更改表名

#菜品分类信息模型
class Category(models.Model):
    shop_id = models.IntegerField()        #店铺id
    name = models.CharField(max_length=50)#分类名称
    status = models.IntegerField(default=1)        #状态:1正常/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    class Meta:
        db_table = "category"  # 更改表名

#菜品信息模型
class Product(models.Model):
    shop_id = models.IntegerField()        #店铺id
    category_id = models.IntegerField()    #菜品分类id
    cover_pic = models.CharField(max_length=50)    #菜品图片
    name = models.CharField(max_length=50)#菜品名称
    price = models.FloatField()    #菜品单价
    status = models.IntegerField(default=1)        #状态:1正常/2停售/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'shop_id':self.shop_id,'category_id':self.category_id,'cover_pic':self.cover_pic,'name':self.name,'price':self.price,'status':self.status,'create_at':self.create_at.strftime('%Y-%m-%d %H:%M:%S'),'update_at':self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "product"  # 更改表名

#会员信息模型
class Member(models.Model):
    nickname = models.CharField(max_length=50)    #昵称
    avatar = models.CharField(max_length=255)    #头像
    mobile = models.CharField(max_length=50)    #电话
    status = models.IntegerField(default=1)        #状态:1正常/2禁用/9删除
    create_at = models.DateTimeField(default=datetime.now)    #创建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间

    def toDict(self):
        return {'id':self.id,'nickname':self.nickname,'avatar':self.avatar,'mobile':self.mobile,'status':self.status}

    class Meta:
        db_table = "member"  # 更改表名

# 订单模型
class Orders(models.Model):
    shop_id = models.IntegerField()   #店铺id号
    member_id = models.IntegerField() #会员id
    user_id = models.IntegerField()   #操作员id
    money = models.FloatField()     #金额
    status = models.IntegerField(default=1)   #订单状态:1过行中/2无效/3已完成
    payment_status = models.IntegerField(default=1)   #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "orders"  # 更改表名


#订单详情模型
class OrderDetail(models.Model):
    order_id = models.IntegerField()  #订单id
    #product_id = models.IntegerField()  #菜品id
    product = models.ForeignKey('Product',on_delete=models.CASCADE) # 多对一
    product_name = models.CharField(max_length=50) #菜品名称
    price = models.FloatField()     #单价
    quantity = models.IntegerField()  #数量
    status = models.IntegerField(default=1) #状态:1正常/9删除

    class Meta:
        db_table = "order_detail"  # 更改表名


# 支付信息模型
class Payment(models.Model):
    order_id = models.IntegerField()  #订单id号
    member_id = models.IntegerField() #会员id
    money = models.FloatField()     #支付金额
    type = models.IntegerField()      #付款方式：1会员付款/2收银收款
    bank = models.IntegerField(default=1) #收款银行渠道:1微信/2余额/3现金/4支付宝
    status = models.IntegerField(default=1) #支付状态:1未支付/2已支付/3已退款
    create_at = models.DateTimeField(default=datetime.now)  #创建时间
    update_at = models.DateTimeField(default=datetime.now)  #修改时间

    class Meta:
        db_table = "payment"  # 更改表名