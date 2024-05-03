from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
@index.route('/index')
def home():
    return render_template('index/index.html')