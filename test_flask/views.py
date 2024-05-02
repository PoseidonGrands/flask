import pymysql
import os

from flask import Blueprint, render_template, request, make_response, jsonify

from test_flask.models import *

# 定义蓝图
index = Blueprint('index', __name__)


@index.route('/get')
def get():
    # name = request.args.get('name', 'null')

    # 统一获取值的方式
    args = request.values
    name = args['name'] if 'name' in args else 'value is null'
    return f'hello, {name}'


@index.route('/post', methods=['post'])
def post():
    name = None
    # try:
    #     name = request.form['name']
    # except:
    #     print('post value error...')
    # return f'hello, {name},(method:{request.method})'

    # 统一获取值的方式
    args = request.values
    name = args['name'] if 'name' in args else 'value is null'
    return f'hello, {name},(method:{request.method})'


@index.route('/file', methods=['post'])
def file():
    f = request.files['file'] if 'file' in request.files else 'null'
    return f'file:{f}'


@index.route('/json')
def json():
    import json
    data = {'name': 'sewell'}
    resp = make_response(json.dumps(data))
    # 需要自己添加请求头
    resp.headers['Content-Type'] = 'application/json'
    return resp

@index.route('/json_same')
def json_same():
    data = {'name': 'sewell'}
    # 不需要自己添加请求头
    resp = make_response(jsonify(data))
    return resp


@index.app_template_filter('phone_format')
def phone_format(tel):
    return tel[0:3] + '****' + tel[:4]

@index.route('/filter')
def filter():
    name = 'sewell'
    phone = '13144135066'
    return render_template('filter.html',
                           name=name,
                           phone=phone)

@index.route('/macro')
def macro():
    name = 'sewell'
    phone = '13144135066'
    return render_template('macro.html',
                           name=name,
                           phone=phone)


@index.route('/search')
def search():
    # 重置逻辑库
    db.drop_all()
    db.create_all()
    # 插入记录
    bonus = Bonus(job='salesman', sal=2000, comm=100)
    bonus2 = Bonus(job='manager', sal=6000, comm=300)
    db.session.add(bonus)
    db.session.add(bonus2)
    db.session.commit()
    # 删除记录
    # bonus_1 = Bonus.query.filter_by(empno='1').first()
    # db.session.delete(bonus_1)
    # db.session.commit()
    # 查询记录
    # 查询全部记录
    res_all = Bonus.query.all()
    # 根据主键找记录
    res = Bonus.query.get(2)
    print(res)
    data = []
    for row in res_all:
        data.append({row.empno: [row.job, row.sal, row.comm]})
        print(__file__)
        print(os.getcwd())
    return f'content:{data}'

@index.route('/list_user/<int:page_index>')
def list_user(page_index):
    """测试分页"""
    # 重置逻辑库
    db.drop_all()
    db.create_all()
    # 插入100条记录
    for i in range(100):
        db.session.add(Bonus(job='salesman', sal=2000 + i, comm=100 + i))
    db.session.commit()
    # 每页数据10条
    per_page = 10
    bonus = Bonus.query
    bonus_page_data = bonus.paginate(page=page_index, per_page=per_page)
    return render_template('list_user.html',
                           bonus_page_data=bonus_page_data)


