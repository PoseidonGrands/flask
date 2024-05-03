from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), nullable=False, unique=True)
    login_name = db.Column(db.String(20), nullable=False)
    login_pwd = db.Column(db.String(20), nullable=False)
    login_salt = db.Column(db.String(20), nullable=False, doc='登录密码随机字符串')
    user_status = db.Column(db.Integer, nullable=False)
    update_time = db.Column(db.Date, nullable=False)
    create_time = db.Column(db.Date, nullable=False)