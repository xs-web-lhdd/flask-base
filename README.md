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
def list_user(page)
```
- URL 中的值为可选
```python
@app.route('/page/<page>')
def list_user(page=None)
```


## 内部视图：
- redirect() 实现重定向
- abort() 处理错误

