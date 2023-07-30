import os.path


class Config(object):
    """项目的配置文件"""
    # 数据库连接 URI
    # 配置数据库连接参数：
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234567890@127.0.0.1/flask_qa'
    # 文件上传的根路径
    MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias')
    # 设置 session 密钥
    SECRET_KEY = 'kdjklfjkd87384hjdhjh'
    # 解决中文乱码
    JSON_AS_ASCII = False
    # JWT 相关配置：
    # config.py
    JWT_SECRET_KEY = "alita666666"


