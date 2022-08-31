from app.db_app import db

class User(db.Model):
    """定义数据模型"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(30))
 
    def __init__(self, username, pwd):
        self.username = username
        self.password = pwd
 
    def __repr__(self):
        return '<User %r>' % self.username