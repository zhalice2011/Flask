#coding:utf8

#定义视图

from . import home
from flask import render_template,redirect,url_for  #render_template加载视图    redirect:是重定向  url_for:是路由生成器

# #注册一个地址
# @home.route("/")
# def index():
#         return render_template("home/index.html")
#


#登录
@home.route("/login/")
def login():
        return render_template("home/login.html")

#注销  ---跳转到home模块下面的login视图
@home.route("/logout/")
def logout():
        return redirect(url_for("home.login"))

#注册
@home.route("/regist/")
def regist():
        return render_template("home/regist.html")


#会员中心
@home.route("/user/")
def user():
        return render_template("home/user.html")

#修改密码
@home.route("/pwd/")
def pwd():
        return render_template("home/pwd.html")

#评论记录
@home.route("/comments/")
def comments():
        return render_template("home/comments.html")

#登录日志
@home.route("/loginlog/")
def loginlog():
        return render_template("home/loginlog.html")

#电影收藏
@home.route("/moviecol/")
def moviecol():
        return render_template("home/moviecol.html")

#首页
@home.route("/")
def index():
        return render_template("home/index.html")

#电影列表页面
@home.route("/animation/")
def animation():
        return render_template("home/animation.html")

#电影搜索页面
@home.route("/search/")
def search():
        return render_template("home/search.html")


#电影详情页面
@home.route("/play/")
def play():
        return render_template("home/play.html")

