from app.db_app import db
from app.db_app.model import User

class Student(User):
    __abstract__ = False
    __tablename__ = "student"
    score = db.Column(db.Integer, nullable=True)