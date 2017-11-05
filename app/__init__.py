#coding:utf8


#创建app对象  然后用app对象去注册蓝图

from flask import Flask,render_template

app = Flask(__name__)  #实例化falsk

app.debug = True #开启调试模式

#导入蓝图对象
from app.home import home as home_blueprint  #从app.home中导入我们的home对象 并且给他取一个名字home_blueprint
from app.admin import admin as admin_blueprint  #从app.admin中导入我们的admin对象 并且给他取一个名字home_blueprint

#开始注册     第一个参数蓝图对象  第二个参数url
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix="/admin")  #这里表示要访问后台的路由需要在前面加上这个/admin


#404的页面
@app.errorhandler(404)
def page_not_found(error):
      return  render_template("home/404.html"), 404