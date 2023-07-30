from flask import Flask, render_template, redirect, current_app, request, make_response
from models import db
from accounts.views import accounts
from qa.views import qa

app = Flask(__name__)
# 从配置文件加载文件
app.config.from_object('config.Config')
# 数据库初始化
db.init_app(app)
# 注册蓝图：
app.register_blueprint(accounts, url_prefix='/accounts')
app.register_blueprint(qa, url_prefix='/qa')


with app.app_context():
    db.create_all()

