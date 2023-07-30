from flask import Blueprint

qa = Blueprint('qa', __name__)


@qa.route('/question')
def login():
    return 'question'

