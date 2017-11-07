#conding:utf8

from flask_wtf import  FlaskForm

#导入三个字段                     密码           表单提交
from wtforms import  StringField,PasswordField,SubmitField

#ValidationError:验证信息错误以后  都需要通过他进行抛出错误
from wtforms.validators import DataRequired,ValidationError

#导入数据模型
from app.models import User


#定义一个后台登录的表单 继承FlaskForm
class LoginForm(FlaskForm):
    """ 管理员登录表单 """
    account = StringField(
        label="账号",   #定义标签名称
        validators=[   #定义账号的验证器
             DataRequired("账号不能为空!")          #不能空
        ],
        description="账号",    #描述:账号
        render_kw={           #附加选项
            "class":"form-control",
            "placeholder":"请输入账号！",
            "required":"required"               #必填项

        }

    )

    #""" 密码 """
    pwd = PasswordField(
        label="密码",  # 定义标签名称
        validators=[  # 定义账号的验证器
            DataRequired("密码不能为空!")  # 不能空
        ],
        description="密码",  # 描述:账号
        render_kw={  # 附加选项
            "class": "form-control",
            "placeholder": "请输入密码！",
            "required": "required"  # 必填项

        }

    )

    #""" 提交 """
    submit = SubmitField(
        '登录',
        render_kw={  # 附加选项
            "class": "btn btn-primary btn-block btn-flat",
            #"required": "required"  # 必填项
        }

    )

    #自定义表单验证器

    def validate_account(self,field):
        account = field.data  #获取传入的账号
        admin = User.query.filter_by(name=account).count()  #从表格里面查询出符合结果的有几条
        if admin == 0: #=0说明没有查到
            raise ValidationError("账号不存在") #抛出一个验证的错误


