from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import constants

# 实例化数据库:
db = SQLAlchemy()


class User(db.Model):
    """用户模型"""
    __tablename__ = 'flask_qa_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    nickname = db.Column(db.String(64))
    password = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(64))
    # 用户是否可以登陆
    status = db.Column(db.SmallInteger, default=constants.UserStatus.USER_ACTIVE.value, comment='用户状态')
    # 是否超级管理员
    is_super = db.Column(db.SmallInteger, default=constants.UserRole.COMMON.value, comment='是否超级管理员')
    birth_data = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)


class UserProfile(db.Model):
    """用户的详细信息"""
    __tablename__ = 'flask_qa_user_profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 冗余字段
    username = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('flask_qa_user.id'))
    # 这个不会在数据库中新加一行，只会在查找时方便查找 user.profile  profile.user
    user = db.relationship('User', backref=db.backref('profile', uselist=False))

