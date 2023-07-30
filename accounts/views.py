from flask import Blueprint

accounts = Blueprint('accounts', __name__)


@accounts.route('/login')
def login():
    return 'hello'


@accounts.route('/register')
def register():
    return 'hello'


@accounts.route('/mine')
def mine():
    return '个人中心'

