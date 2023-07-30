# flask:
官网：https://flask.net.cn/installation.html

MTV：
- Model：Flask-PyMongo、Flask-MongoKit、Flask-SQLAlchemy
- Templates：Flask-WTF、Flask-Uploads、bootstrap-flask
- View：Jinja2

```python
# flask 1.0 之前的启动服务器的方式，1.0之后就不推荐了
from flask import Flask, render_template

app = Flask(__name__)


# 添加装饰器：
@app.route('/')
@app.route('/index')
def Hello_world():
    return 'hello world!'


@app.route('/user')
def user():
    user = {
        'name': '张三'
    }
    return render_template('hello.html', user=user)

if __name__ == '__main__':
    print('服务准备启动...')
    app.run()
    print('服务启动完成...')

```

## 启动服务器：
- 步骤一：设置环境变量：
  - windows：set FLASK_APP=flasker.py
  - linux: export FLASK_APP=flasker.py
- 步骤二：flask run启动内置web服务器指定IP及端口：
  - flask run --host=0.0.0.0 --port=8081 或者 flask run -h 0.0.0.0 -p 8001

## 开启调试模式：
代码修改后服务器自动重启
- 步骤1：设置环境变量
  - windows: set FLASK_ENV=development
  - linux: export FLASK_ENV=development
- 步骤二：flask run启动内置web服务器指定IP及端口：
  - flask run --host=0.0.0.0 --port=8081 或者 flask run -h 0.0.0.0 -p 8001

## flask 扩展包：
网址：https://pypi.org/

## URL 与 配置路由：
- 方式一：使用装饰器 @app.route(url_name, methods)
- 方式二：使用 API 配置 app.add_url_rule(url, url_name, view_name)

### 方式一：使用装饰器
- 语法规则 @app.route(url, methods)
- 参数解释
  - url: 匹配的 URL 地址
  - methods：所支持的请求方式 (['GET', 'POST'])
- 示例：@app.route('/login', methods=['GET', 'POST'])

### 使用 API 配置（不常用）
- 语法规则 app.add_url_rule(url, url_name, view_name)
- 参数解释：
  - url: 匹配的 URL 地址
  - url_name：给URL的命名
  - view_name: 视图函数

### 路由匹配规则：
- 匹配整个文字 @app.route('/hello')
- 传递参数 @app.route('/user/<username>')
- 指定参数类型 @app.route('/post/<int:post_id>')

### URL配置及路由：
- 查看URL规则列表 app.url_map
- URL 逆向解析（根据名称解析成URL字符串）
  - url_for(url_name, **kwargs)
  - url_for('static', filename='style.css')

### 视图函数中获取页面传值
- URL 中的值
```python
@app.route('/page/<page>')
def list_user(page):
```
- URL 中的值为可选
```python
@app.route('/page/<page>')
def list_user(page=None):
```

## 请求报文：
- method：请求的类型
- form：POST请求数据dict
- args：GET请求数据dict
- values：POST请求和GET请求数据集合dict
- files：上传的文件数据dict
- cookies：请求中的cookie dict
- headers：HTTP请求头

### 请求钩子：
- before_first_request 服务器初始化后第一个请求到达前执行
- before_request 每一个请求到达前
- after_request 每次请求处理完成后执行，如果请求过程中产生了异常，则不执行
- teardown_request 每一次请求处理完成之后执行，如果请求过程中产生了异常页执行

## 响应报文：
- 响应元组：
  - 1、response 响应内容
  - 2、status 相应状态码
  - 3、headers 响应头信息

## 内部视图：
- redirect() 实现重定向
- abort() 处理错误



## 数据库：
flask-sqlalchemy 官网: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
### 数据库安装和配置：
- 使用 flask-sqlalchemy 配置
- 安装：
```shell
pip install -U flask-sqlalchemy
pip install mysqlclient
```
- 配置数据库连接参数：
```python 
# 配置数据库连接参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/test_flask'
# 多个数据库支持
SQLALCHEMY_BINDS= {
  'db1': 'mysqldb://localhost/users',
  'db2': 'sqlite:////path/to/appmeta.db'
}
```
在数据库可视化软件中创建数据库 test_flask
### 数据库模型设计：
- 绑定到 Flask 对象 `db = SQLAlchemy(app)`
- ORM模型创建
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```
- 指定表的名称：`__tablename__='weibo_user'`

#### 创建和删除表：
- 手动创建数据库
- 创建表，一个数据库时可以不传参数，多个数据库传参数指定绑定那个数据库 `db.create_all(bind='db1')`
- 删除表 ``db.drop_all()``
```python
# 示例代码;
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库连接参数：
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567890@127.0.0.1/test_flask'
# 实例化数据库
db = SQLAlchemy(app)


# 设计模型：
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)

# 这里使用 with app.app_context(): 否则报错
with app.app_context():
    db.create_all()  # 创建所有数据表
```

#### 一对多关系，外键关联
user = db.relationship('User', backref=db.backref('address', lazy=True))

### 数据库操作：
#### 新增/修改数据：
- 构造 ORM 模型对象：user = User('admin', 'admin@example.com')
- 添加到 db.session（备注：可添加多个对象）：db.session.add(user)
- 提交到数据库：db.session.commit()

#### 物理删除数据：
- 查询 ORM 模型对象：user = User.query.filter_by(username='zhangsan').first()
- 添加到db.session： db.session.delete(user)
- 提交到数据库：db.session.commit()

#### ORM 查询：
- 返回结果集（list）
  - 查询所有数据： 
    - User.query.all()
  - 按条件查询：
    - User.query.filter_by(username='zhangsan')
    - User.query.filter(User.nickname.endswith('三')).all()
  - 排序：
    - User.query.order_by(User.username)
  - 查询TOP10：
    - User.query.limit(10).all()

- 返回单个 ORM 对象
  - 根据 主键 查询：
    - User.query.get(1) 这里的 1 是主键是 id，是 int 类型，所以为 1
  - 获取第一条记录：
    - user.query.first()

- 视图快捷函数：有则返回，无则返回 404
  - first() vs first_or_404()
  - get() vs get_or_404()

- 多表关联查询
  - db.session.query(User).join(Address)
  - User.query.join(Address)

#### 分页：
- 方式一：使用 offset 和 limit
  - .offset(offset).limit(limit) 
方式二：paginate分页支持
  - .paginate(page=2, per_page=4)
  - Pagination对象：
    - has_prev/has_next 是否有上一页/下一页
    - items 当前页的数据列表
    - prev_num/next_num 上一页/下一页的页码
    - total 总记录数
    - pages 总页数
  

### 文件名称格式化:
werkzegu.utils.secure_filename


## 蓝图:
### 蓝图是什么
- 大型应用组织管理
- 模块化/组件化
- 一个项目可以有多个蓝图

### 蓝图的实现过程
- 第一步: 按模块拆分
  ORM模型、配置、常量、工具类、功能模块等
- 第二步：视图文件中，实例化一个蓝图对象
```python
accounts = Blueprint('accounts', __name__, templates_folder='templates', static_floder='static')
```
- 第三步：注册蓝图
```python
from accounts.views import accounts
app.register_blueprint(accounts, url_prefix='/accounts')
```
