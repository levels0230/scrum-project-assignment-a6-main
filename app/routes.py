from flask import Blueprint, request, render_template, session, redirect, url_for, flash

from app.tea_app.model import Teacher
from app.stu_app.model import Student
from app.db_app import db

bp = Blueprint('all', __name__, url_prefix="/r")

@bp.route('/index', endpoint='index', methods=['GET'])
def index():
    if session.get('role') == 'teacher':
        return redirect(url_for('teacher.index'))
    elif session.get('role') == 'student':
        return redirect(url_for('student.index'))
    return render_template("index.html")

@bp.route('/register', endpoint='register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        role = request.form['role']
        username = request.form['username']
        password = request.form['password']
        print(role, username, password, flush=True)
        if role == 'teacher':
            teacher = Teacher.query.filter(Teacher.username == username).first()
            if teacher:
                flash('Username already taken! Please change username')
                return redirect(url_for('all.index'))
            teacher = Teacher(username=username, pwd=password)
            db.session.add(teacher)
            db.session.commit()
            flash('registration success! please sign in!')
            return redirect(url_for('all.index'))
            
        else:
            student = Student.query.filter(Student.username == username).first()
            if student:
                flash('Username already taken! Please change username')
                return redirect(url_for('all.index'))
            student = Student(username=username, pwd=password)
            db.session.add(student)
            db.session.commit()
            flash('registration success! please sign in!')
            return redirect(url_for('all.index'))


@bp.route('/logout', endpoint='logout', methods=['GET'])
def logout():
    if session.get('username'):
        session.clear()
    return redirect(url_for('all.index'))