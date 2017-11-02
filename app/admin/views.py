#coding:utf8

#定义视图

from . import admin

#注册一个地址
@admin.route("/")  #调用路由
def index():
        return "<h1 style='color:blue'>admin 我是</h1>"