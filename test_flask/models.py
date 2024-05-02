from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Bonus(db.Model):
    __tablename__ = 't_bonus'
    empno = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(20))
    sal = db.Column(db.Integer)
    comm = db.Column(db.Numeric(10, 2))