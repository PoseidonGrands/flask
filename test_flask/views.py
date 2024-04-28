from flask import Blueprint, render_template

# 定义蓝图
index = Blueprint('index', __name__)


@index.route('/get')
def get():
    return 'hellosssss'