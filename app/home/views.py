#coding:utf8

#定义视图

from . import home

#注册一个地址
@home.route("/")
def index():
        return "<h1 style='color:red'>home 我是</h1>"




# if __name__ == "__main__":
#     app.run()