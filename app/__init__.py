from flask import Flask
from app.db_app import db
from app.db_app import bp as db_bp
from flask_migrate import Migrate
from flask import redirect, url_for

from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView

from app.routes import bp as all_bp
from app.stu_app import bp as stu_bp
from app.tea_app import bp as tea_bp

from app.tea_app.model import Teacher, Question
from app.stu_app.model import Student

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

__version__ = '0.0.1'

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app=app)

Migrate(app, db)

admin = Admin(app,name=u'Background management system')

# from app.tea_app.model import Teacher


app.register_blueprint(db_bp)
app.register_blueprint(all_bp)
app.register_blueprint(stu_bp)
app.register_blueprint(tea_bp)

# engin = create_engine(config.DB_URI)
# session = Session(engin)

admin.add_view(ModelView(Teacher, db.session,endpoint='TeacherClass'))
admin.add_view(ModelView(Student, db.session,endpoint='StudentClass'))
admin.add_view(ModelView(Question, db.session,endpoint='QuestionClass'))


@app.route('/')
def index_route():
    return redirect(url_for('all.index'))