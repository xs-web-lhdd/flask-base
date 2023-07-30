from flask import Flask, render_template, redirect, current_app, request, make_response
from flask_sqlalchemy import SQLAlchemy

# 文件名称格式化:

app = Flask(__name__)

# 配置数据库连接参数：
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567890@127.0.0.1/test_flask'
# 实例化数据库
db = SQLAlchemy(app)


# 设计模型：
class User(db.Model):
    # 设置表名称，不设置就是 class 名字
    __tablename__ = 'test_flask_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    birth_data = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, nullable=True)


class UserAddress(db.Model):
    """用户地址"""
    __tablename__ = 'test_flask_useraddress'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('test_flask_user.id'), nullable=False)
    # 这个不会在数据库中新加一行，只会在查找时方便查找
    user = db.relationship('User', backref=db.backref('address', lazy=True))


def addUser(id, username, password):
    user = User(id=id, username=username, password=password)
    db.session.add(user)
    db.session.commit()


def deteleUser(username):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()


def getAllUser():
    all_user = User.query.all()
    print('all_user', all_user)


def getUserByUsername(username):
    user = User.query.filter_by(username=username)
    print('getUserByUsername', user)


def getUserByEnd(char):
    user = User.query.filter(User.username.endswith(char)).all()
    print('getUserByEnd', user)


def addUserByNum(num):
    for i in range(num):
        user = User(username='user_{}'.format(i), password='password_{}'.format(i))
        db.session.add(user)
    db.session.commit()


def deleteUserByNum(num):
    for i in range(num):
        user = User.query.filter_by(username='user_{}'.format(i)).first()
        db.session.delete(user)
    db.session.commit()


with app.app_context():
    # 创建表/删除表
    # db.create_all()  # 创建所有数据表
    # db.drop_all()
    # 增删
    # addUser(3, '111', '2222')
    # deteleUser('111')
    # 查询
    # getAllUser()
    # getUserByUsername('刘豪')
    # getUserByEnd('杰')
    # addUserByNum(100)
    deleteUserByNum(100)


@app.route('/index')
def index():
    print(current_app)
    return 'index'


@app.route('/test/req')
def t_request():
    """请求报文练习"""
    get_args = request.args
    print(get_args)
    name = request.args.get('name')
    print('name is {}'.format(name))
    return 'request success'


# @app.before_first_request
# def first_request():
#     """服务器启动后第一个请求到达"""
#     print('服务器启动后第一个请求到达 first_request')


@app.before_request
def per_request():
    """每一个请求到达前："""
    print('每一个请求到达前。。。')


"""响应"""


@app.route('/test/resp')
def t_response():
    """测试响应"""
    # return 'response success', 401, {
    #     'user_id': 'my_user_id'
    # }

    # 构造一个响应对象
    # resp = make_response('这是一个响应对象', 403, {
    #     'token': 'ABC123'
    # })
    # resp.headers['user_id'] = 'my_user_id'
    # resp.status_code = 200

    # 响应 html
    html = "<html><body><h1>你好伟杰！</和></body></html>"
    resp = make_response(html)
    return resp


# 添加装饰器：
@app.route('/')
@app.route('/index')
def Hello_world():
    return 'hello world!111'


@app.route('/user')
def user():
    # 视图函数：
    user = {
        'name': '张三'
    }
    return render_template('hello.html', user=user)


@app.route('/user/<page>')
def list_user(page=1):
    return '您好，您是第 {} 页的用户'.format(page)


def login():
    return '登陆成功！'


# 第二中路由写法：
app.add_url_rule('/login', 'login', login)

# 不推荐：
# if __name__ == '__main__':
#     print('服务准备启动...')
#     app.run()
#     print('服务启动完成...')
