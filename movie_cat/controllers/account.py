from flask import Blueprint, render_template

from movie_cat.models import db

# 定义蓝图
account = Blueprint('account', __name__)

@account.route('/login')
def login():
    return render_template('account/login.html')

@account.route('/reg')
def reg():
    return render_template('account/reg.html')


@account.route('/init_tables')
def init_tables():
    db.drop_all()
    db.create_all()
    return 'aaa'



