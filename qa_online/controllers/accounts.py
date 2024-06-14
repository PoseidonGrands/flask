from flask import Blueprint, render_template, request, flash

from qa_online.forms.reg import RegForm
from qa_online.model import User, UserProfile, db

accounts = Blueprint('accounts', __name__)

@accounts.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            username = form.username.data
            nickname = form.nickname.data
            password = form.password.data
            user = User(username=username, nickname=nickname, password=password)
            user_profile = UserProfile(username=username, user=user)
            db.session.add(user)
            db.session.add(user_profile)
            db.session.commit()
            flash('成功注册', 'success')
        except Exception as e:
            print(e)
            flash('注册失败', 'danger')

    return render_template('accounts/register.html', form=form)

@accounts.route('/login')
def login():
    return render_template('accounts/login.html')

