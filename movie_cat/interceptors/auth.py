from movie_cat.app import app
from flask import request, g

from movie_cat.common.user_service import UserService
from movie_cat.models import User


@app.before_request
def before_request():
    app.logger.info('----before_request-----')
    g.current_user = None
    # 校验cookie
    user_info = check_cookie()
    if user_info:
        g.current_user = user_info
    app.logger.info(user_info)


def check_cookie():
    """没有验证cookiename是否一致
    没有验证cookie根据符号分割开数组长度是否符合要求
    查询到的对象有可能为None，没校验
    查询可能有异常，没做try
    """
    # 解析出标志位，用来再次生成cookie对比存储的cookie是否正确
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    # 1、检查请求的cookie的name是否存在
    auth_cookie = cookies[cookie_name] if cookie_name in cookies else None
    if auth_cookie is None:
        return False

    # 2、检查cookie分割后的长度.
    cookie_info = auth_cookie.split('-')
    if len(cookie_info) != 2:
        return False

    # 3、用标志位从数据库查询数据并再次生成cookie对比
    try:
        user_info = User.query.filter_by(id=cookie_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if cookie_info[0] != UserService.gene_auth(user_info):
        return False

    return user_info