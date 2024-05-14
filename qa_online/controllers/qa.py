from flask import Blueprint, render_template

qa = Blueprint('qa', __name__)

@qa.route('/')
def index():
    return render_template('qa/index.html')

@qa.route('/follow')
def follow():
    return render_template('qa/follow.html')


@qa.route('/write')
def write():
    return render_template('qa/write.html')

@qa.route('/mine')
def mine():
    return render_template('qa/mine.html')

@qa.route('/detail')
def detail():
    return render_template('qa/detail.html')
