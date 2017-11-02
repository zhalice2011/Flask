# coding:utf8
# 导入蓝图
from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views  # 导入views的内容
