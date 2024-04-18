from flask import flash, render_template, redirect
from .. import login_manager
from ..db import User, Session
from sqlalchemy import select
from ..forms import RegisterForm, LoginForm
from .. import app


@login_manager.user_loader
def load_user(user_id):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.id == user_id))
        return user
    

@app.get('/register')
def register():
    form = RegisterForm()
    return render_template('form_template.html', form=form)

@app.post('/register')
def register_post():

    form = RegisterForm()
    if form.validate_on_submit():
       with Session.begin() as session:
           user = session.scalar(select(User).where(User.email == form.email.data))
           if user:
               flash("User exists!")
               return redirect('register')
           pwd = form.password.data
           user = User(
               nickname = form.email.data.split('@')[0],
               email = form.email.data,
               password = pwd,
           )
           session.add(user)

       return redirect('login')
    return redirect('register')


@app.get('/login')
def login():
    form = LoginForm()
    return render_template('form_template.html', form=form)
