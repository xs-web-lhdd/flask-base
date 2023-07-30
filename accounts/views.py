import hashlib

from flask import Blueprint, request, jsonify, session

import constants
from models import User, UserProfile, db, UserLoginHistory
from utils.json_web_token import create_token, verify_jwt
from utils.utils import model_to_dict

accounts = Blueprint('accounts', __name__)


@accounts.route('/login', methods=['POST'])
def login():
    """用户注册"""
    # 1、获取表单信息
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    password = hashlib.sha256(password.encode()).hexdigest()
    # 2、查询用户信息，如果密码错误不能登陆，用户状态被锁也不能登陆
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        return jsonify({
            "code": 200,
            "data": {
                "msg": "账号或密码错误！"
            }
        })
    if user.status == constants.UserStatus.USER_IN_ACTIVE.value:
        return jsonify({
            "code": 200,
            "data": {
                "msg": "账号已经被禁用，请联系管理员进行启用账号！"
            }
        })
    # 3、正式登陆
    # session['user_id'] = user.id
    # 4、记录登陆日志
    ip = request.remote_addr
    ua = request.headers.get('user-agent', None)
    login_obj = UserLoginHistory(username=username, ip=ip, ua=ua, user=user)
    db.session.add(login_obj)
    db.session.commit()

    print('登陆成功！')
    user_info = model_to_dict(user)
    token = create_token(username, password)
    user_info['token'] = token
    return user_info


@accounts.route('/register', methods=['POST'])
def register():
    """用户注册"""
    # 1、获取表单信息
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    nickname = data.get('nickname')
    # 2、查询有无次人，无人再注册，有人就不注册提示已经注册过
    user = User.query.filter_by(username=username).first()
    if user is None:
        # 3、添加到 db.session
        # 密码加密：
        password = hashlib.sha256(password.encode()).hexdigest()
        user_obj = User(username=username, password=password, nickname=nickname)
        db.session.add(user_obj)
        profile = UserProfile(username=username, user=user_obj)
        db.session.add(profile)
        db.session.commit()
        return jsonify({
            "code": 200,
            "data": {
                "token": "666666"
            }
        })
    else:
        return jsonify({
            "code": 200,
            "data": {
                "msg": "此用户已经注册过了！"
            }
        })


@accounts.route('/logout', methods=['POST'])
def logout():
    """退出登陆"""


@accounts.route('/upload', methods=['POST', 'OPTIONS'])
def uploadAvatar():
    """上传图片"""
    token = request.headers
    print(token)
    # payload = verify_jwt(token)
    # print(payload)
    # 取出头像
    avatar = request.files['file']
    try:
        avatar.save('./medias/{}'.format(avatar.filename))

        return jsonify({
            'code': 200,
            'message': '上传头像成功'
        })
    except IOError:
        return jsonify({
            'code': 200,
            'message': '上头头像失败！请重试！'
        })




@accounts.route('/mine')
def mine():
    return '个人中心'
