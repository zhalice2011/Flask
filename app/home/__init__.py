# coding:utf8
# 导入蓝图
from flask import Blueprint

home = Blueprint("home", __name__)

import app.home.views  # 从app.home.view里面导入views的内容
