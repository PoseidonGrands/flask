from datetime import datetime

from flask import Blueprint, render_template, request

from movie_cat.common.utils import response_error_json, response_json, gene_pwd, gene_salt
from movie_cat.models import db, User

# 定义蓝图
account = Blueprint('account', __name__)

@account.route('/login')
def login():
    return render_template('account/login.html')

@account.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('account/reg.html')
    # POST方式提交校验数据并返回JSON格式的数据
    data = request.values
    login_name = data['login_name'] if 'login_name' in data else ''
    login_pwd = data['login_pwd'] if 'login_pwd' in data else ''
    repeat_pwd = data['repeat_pwd'] if 'repeat_pwd' in data else ''
    if login_name is None or len(login_name) < 1:
        return response_error_json('请输入用户名')
    else:
        # 查询数据库是否有该用户名
        user = User.query.filter_by(login_name=login_name).first()
        print(User.query.filter_by(login_name=login_name))
        if user:
            return response_error_json('该用户名已经注册')
    if login_pwd is None or len(login_pwd) < 1:
        return response_error_json('请输入密码')
    if repeat_pwd != login_pwd:
        return response_error_json('请再次输入密码')

    # 入库
    user = User()
    user.login_name = login_name
    user.nickname = login_name
    # 加密密码
    salt = gene_salt()
    user.login_salt = salt
    user.login_pwd = gene_pwd(login_pwd, salt)
    user.user_status = 1
    user.create_time = user.update_time = datetime.now()

    db.session.add(user)
    db.session.commit()

    return response_json(msg='注册成功，点击跳转...', data={'login_name': login_name,'login_pwd': login_pwd, 'repeat_pwd': repeat_pwd})



@account.route('/init_tables')
def init_tables():
    db.drop_all()
    db.create_all()
    return 'aaa'



