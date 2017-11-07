#coding:utf:8

#这个文件用来定义数据模型
#from app import db  #将db导入进来
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from datetime import  datetime
import pymysql

app = Flask(__name__)  #实例化falsk

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:8889/movie"  #定义一个数据的连接  连接数据库

app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = True  #如果设置成true 就会追踪对象

#app.config["SECRET_KEY"] = "29c5f4f9394d4f6893cea96cd08874ac"  #如果设置成true 就会追踪对象


#app.debug = True #开启调试模式

db = SQLAlchemy(app)


#首先定义一个会员的模型  unique=True表示唯一
#继承的是db.model
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    phone = db.Column(db.String(11),unique=True)
    info = db.Column(db.Text)  #表示文本类型
    face = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    uuid = db.Column(db.String(255),unique=True)
    userlogs = db.relationship("Userlog",backref="user") #会员日志外键关系的关联
    comments = db.relationship("Comment",backref="user") #关联到评论
    moviecols = db.relationship("Moviecol",backref="user") #关联到收藏


    def __repr__(self):
        return "<User %r>" % self.name


#定义会员登录日志
class Userlog(db.Model):  # 继承的是db.model
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  #primay_key主键
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))    #关联user表格里面的id
    ip = db.Column(db.String(100)) #登录ip
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow) #登录时间

    #查询的时候返回一个格式 %r 表示占位符
    def __repr__(self):
        return "<Userlog %r>" % self.id



#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    name = db.Column(db.String(100), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    movies = db.relationship("Movie",backref='tag')  #电影外键的关系的一个关联

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Moive(db.Model):
    __tablename__ = "moive"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    name = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True) #封面
    star = db.Column(db.SmallInteger)   #SmallInteger小整形
    palynum = db.Column(db.BigInteger)   #播放量
    commentnum = db.Column(db.BigInteger)   #播放量
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))   #通过这个标签去关联这个表格
    area = db.Column(db.String(255), unique=True)
    area = db.Column(db.String(100)) #电影长度
    length = db.Column(db.Date)  # 上映时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    comments = db.relationship("Commnet", backref='moive')  # 评论外键的关系的一个关联  关联到评论的这个表格
    moviecols = db.relationship("Moviecol", backref='moive')  # 收藏外键的关系的一个关联  关联到评论的这个表格

    def __repr__(self):
        return "<Movie %r>" % self.title

#预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title

#评论
class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    content = db.Column(db.Text) #评论内容
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id')) #关联到我们的movieid  指向所属的电影
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #关联到我们的userid  指向所属的用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id


#电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id')) #关联到我们的movieid  指向所属的电影
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #关联到我们的userid  指向所属的用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Moviecol %r>" % self.id


#权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    name = db.Column(db.String(100),unique=True) # 名称
    url = db.Column(db.String(255),unique=True) # 地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name  #查询返回name


#角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # primay_key主键
    name = db.Column(db.String(100),unique=True) # 名称
    auths = db.Column(db.String(600)) # 列表
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name  #查询返回name

#管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  #编号
    name = db.Column(db.String(100), unique=True) #管理员账号
    pwd = db.Column(db.String(100))               #管理员密码
    is_super = db.Column(db.SmallInteger)   #小整形 是否为超级管理员  0表示为超级管理员
    role_id = db.Column(db.Integer,db.ForeignKey('role.id')) #关联到我们的roleid  指向所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    adminlogs = db.relationship("Adminlog",backref="admin") #关联到登录日志
    oplogs = db.relationship("Oplog",backref="admin") #关联到登录日志


    def __repr__(self):
        return "<Admin %r>" % self.name
#管理员登录日志
class Adminlog(db.Model):  # 继承的是db.model
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  #编号
    user_id = db.Column(db.Integer,db.ForeignKey('admin.id'))    #所属管理云
    ip = db.Column(db.String(100)) #登录ip
    addtime = db.Column(db.DateTime,index=True,default=datetime.utcnow) #登录时间

    #查询的时候返回一个格式 %r 表示占位符
    def __repr__(self):
        return "<Adminlog %r>" % self.id

#管理员操作日志

class Oplog(db.Model):  # 继承的是db.model
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理云
    ip = db.Column(db.String(100))  # 登录ip
    reason = db.Column(db.String(600))  # 操作的原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 登录时间

    # 查询的时候返回一个格式 %r 表示占位符
    def __repr__(self):
        return "<Oplog %r>" % self.id



# 将上面的模型生成我们的mysql数据表

if __name__ == "__main__":
    db.create_all()