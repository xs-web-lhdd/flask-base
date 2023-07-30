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
app.register_blueprint(accounts, url_prefix='/api/accounts')
app.register_blueprint(qa, url_prefix='/api/qa')



# 跨域支持
# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Access-Control-Allow-Headers'] = '*'
#     resp.headers['Access-Control-Allow-Methods'] = '*'
#     return resp
#
#
# app.after_request(after_request)

# with app.app_context():
#     db.create_all()

# @app.before_request
# def jwt_authentication():
#     """
#     1.获取请求头Authorization中的token
#     2.判断是否以 Bearer开头
#     3.使用jwt模块进行校验
#     4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
#     """
#     auth = request.headers.get('Authorization')
#     if auth and auth.startswith('Bearer '):
#         "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符"
#         token = auth[7:]
#         try:
#             "判断token的校验结果"
#             payload = jwt.decode(token, SALT, algorithms=['HS256'])
#             "获取载荷中的信息赋值给g对象"
#             g.username = payload.get('username')
#         except exceptions.ExpiredSignatureError:  # 'token已失效'
#             g.username = 1
#         except jwt.DecodeError:  # 'token认证失败'
#             g.username = 2
#         except jwt.InvalidTokenError:  # '非法的token'
#             g.username = 3
