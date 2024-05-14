from flask import Blueprint, render_template

accounts = Blueprint('accounts', __name__)

@accounts.route('/reg')
def reg():
    return render_template('accounts/register.html')

@accounts.route('/login')
def login():
    return render_template('accounts/login.html')

