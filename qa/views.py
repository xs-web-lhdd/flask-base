from flask import Blueprint, request, make_response

from models import Question

qa = Blueprint('qa', __name__)


@qa.route('/question')
def login():
    return 'question'


@qa.route('/follow')
def follow():
    """关注"""
    # 每页数据的大小
    per_page = 20
    # 当前页码，默认是 1
    page = request.args.get('page', 1)
    print('page ------------->>>>>>>>>>>>>>>>>>>>')
    page_data = Question.query.filter_by(is_valid=False).paginate(page=page, per_page=per_page)
    print('page_data ------》》》》》》》', page_data)
    return make_response(page_data, 200)


