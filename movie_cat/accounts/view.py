from flask import Blueprint

from movie_cat.models import db

# 定义蓝图
account = Blueprint('account', __name__)

@account.route('/login')
def login():
    return ''


@account.route('/create_tables')
def create_tables():
    db.create_all()
    return 'aaa'


@account.route('/drop_tables')
def drop_tables():
    db.drop_all()
    return 'aa'