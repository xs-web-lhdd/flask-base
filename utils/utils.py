"""封装工具函数文件"""


# 将数据库单个对象转化为 dict 格式
def model_to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


# 将一组数据库对象数据转为 list 格式
def scalars_to_list(obj):
    return [model_to_dict(c) for c in obj]
