from contextlib import redirect_stderr
from xmlrpc.client import TRANSPORT_ERROR
from app.tea_app import bp
from flask import render_template, request, flash, redirect, url_for, session
from .model import Question, Teacher
from app.db_app import db

@bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", title='教师登录')
    else:
        username = request.form['username']
        password = request.form['password']
        # from app.db_app import db
        teacher = Teacher.query.filter(Teacher.username == username).first()
        if teacher and password == teacher.password:
            session['role'] = 'teacher'
            session['username'] = username
            session['id'] = teacher.id
            return redirect(url_for('teacher.index'))
        else:
            session.clear()
            flash('未找到该用户名或密码错误')
            return redirect(url_for('teacher.login'))

@bp.route('/index', endpoint='index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if Teacher.query.filter(Teacher.username == session.get('username')).first():
            print(session.get('username'), flush=True)
            if session.get('role') == 'teacher':
                questions = Question.query.filter(Question.designer == session.get('id')).all()
                # return '教师首页' + str(session.get('id')) + str([q.context+', ' for q in questions])
                for q in questions:
                    teacher = Teacher.query.filter(Teacher.id == q.designer).first()
                    if teacher:
                        q.designer = teacher.username
                return render_template('teacher.html', questions=questions, username=session.get('username'))
            else:
                return redirect(url_for('student.index'))
        else:
            session.clear()
            return redirect(url_for('all.index'))
    elif request.method == 'POST':
        if session.get('role') != 'teacher':
            return redirect(url_for(all.index))
        context = request.form['context']
        answer = request.form['answer']
        q_type = request.form['type']
        q_level = request.form['level']
        
        try:
            designer = int(session.get('id'))
            question = Question(designer=designer, context=context, answer=answer, q_type=q_type, q_level=q_level)
            db.session.add(question)
            db.session.commit()
        except Exception as e:
            # print('添加出错', e, flush=True)
            pass
        return redirect(url_for('teacher.index')) 

