from app.db_app import db
from app.db_app.model import User

class Teacher(User):
    __abstract__ = False
    __tablename__ = "teacher"

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    designer = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    context = db.Column(db.String(300), unique=True)
    answer = db.Column(db.String(300))
    q_type = db.Column(db.String(20))
    q_level = db.Column(db.Integer)
    teacher = db.relationship('Teacher', backref='question')

    def __init__(self, designer, context, answer, q_type, q_level):
        self.designer = designer
        self.context = context
        self.answer = answer
        self.q_type = q_type
        self.q_level = q_level
 
    def __repr__(self):
        return '<Question %r>' % self.context