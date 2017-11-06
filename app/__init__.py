#coding:utf8


#创建app对象  然后用app对象去注册蓝图

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  #实例化falsk

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:8889/movie"  #定义一个数据的连接  连接数据库

app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = True  #如果设置成true 就会追踪对象

app.config["SECRET_KEY"] = "29c5f4f9394d4f6893cea96cd08874ac"  #如果设置成true 就会追踪对象


app.debug = True #开启调试模式

db = SQLAlchemy(app)


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


