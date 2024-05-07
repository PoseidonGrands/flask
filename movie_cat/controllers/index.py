from flask import Blueprint, render_template, session

from movie_cat.common.utils import ops_render

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/index')
def home():
    return ops_render('index/index.html')