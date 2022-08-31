from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

bp = Blueprint('db', __name__, url_prefix='/db')

from . import views
from app.stu_app.model import Student
from app.tea_app.model import Teacher
from app.tea_app.model import Question