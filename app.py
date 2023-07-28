from flask import Flask, render_template, redirect

app = Flask(__name__)


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
