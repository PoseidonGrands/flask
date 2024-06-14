from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class RegForm(FlaskForm):
    username = StringField(label='', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入用户名'
    })
    nickname = StringField(label='', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入昵称'
    })
    password = PasswordField(label='', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入密码'
    })
    confirm_password = PasswordField(label='', render_kw={
        'class': 'form-control input-lg',
        'placeholder': '请输入确认密码'
    })