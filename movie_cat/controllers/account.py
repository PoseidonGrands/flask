from datetime import datetime

from flask import Blueprint, render_template, request, session, make_response, redirect

from movie_cat.common.user_service import UserService
from movie_cat.common.utils import response_error_json, response_json
from movie_cat.models import db, User

# 定义蓝图
account = Blueprint('account', __name__)

@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('account/login.html')
    else:
        data = request.values
        login_name = data['loginName'] if 'loginName' in data else ''
        login_pwd = data['loginPwd'] if 'loginPwd' in data else ''

        if login_name is None or login_pwd is None or len(login_name) < 3 or len(login_name) < 3:
            return response_error_json('账户名或密码长度小于3位，请重新输入')

        # 数据符合要求，查询数据库
        user = User()
        user_info = user.query.filter_by(login_name=login_name).first()
        # 该用户能查询到则进行密码验证，用密码生成md5字段看是否符合
        if not user or UserService.gene_pwd(login_pwd, user_info.login_salt) != user_info.login_pwd:
            return response_error_json('请输入正确的登录名和密码')

        # 账户状态检查
        if user_info.user_status != 1:
            return response_error_json('账户被禁用了')

        # 生成cookie
        response = make_response(response_json())
        from movie_cat.app import app
        # 30天有效期
        response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                            f'{UserService.gene_auth(user_info)}-{user_info.id}',
                            60 * 60 * 24 * 30)

        return response


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
    salt = UserService.gene_salt()
    user.login_salt = salt
    user.login_pwd = UserService.gene_pwd(login_pwd, salt)
    user.user_status = 1
    user.create_time = user.update_time = datetime.now()

    db.session.add(user)
    db.session.commit()

    return response_json(msg='注册成功，点击跳转...', data={'login_name': login_name,'login_pwd': login_pwd, 'repeat_pwd': repeat_pwd})

@account.route('/logout')
def logout():
    # redirect()
    pass

@account.route('/init_tables')
def init_tables():
    db.drop_all()
    db.create_all()
    return 'aaa'



