from app.stu_app import bp
from flask import render_template, request, redirect, url_for, flash, session
from app.stu_app.model import Student

@bp.route('/login', endpoint='login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html", title='Student Login')
    else:
        username = request.form['username']
        password = request.form['password']
        student = Student.query.filter(Student.username == username).first()
        if student and password == student.password:
            session['role'] = 'student'
            session['username'] = username
            return redirect(url_for('student.index'))
        else:
            session.clear()
            flash('The username was not found or the password is incorrect')
            return redirect(url_for('student.login'))

@bp.route('/index', endpoint='index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('username'):
            if session.get('role') == 'student':
                return 'Student Home'
            else:
                return redirect(url_for('teacher.index'))
        else:
            return redirect(url_for('all.index'))