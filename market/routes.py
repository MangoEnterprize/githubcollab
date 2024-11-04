from market import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

# this is root url, can handle mulriple decorators
@app.route('/') 
@app.route('/home')
def home_page():
    return render_template('home.html')

# dynamic route takes username
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'

@app.route('/jobs')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('home.html', items=items)

@app.route('/job')
def jobs_page():
    return render_template('job.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        # login registered user
        login_user(user_to_create)
        flash(f'Account created, logged as: {user_to_create.username}', category='success')
            

        return redirect(url_for('home_page'))
    
    if form.errors: #if no errors from validation
        for error in form.errors.values():
            flash(f'there was an error: {error}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # verify user exists and password correct
        attemptedUser = User.query.filter_by(username=form.username.data).first()
        if attemptedUser and attemptedUser.check_password_correction(
            attempted_password=form.password.data
        ): 
            login_user(attemptedUser)
            flash(f'Success, login as: {attemptedUser.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash("Failed login", category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You logged out", category='info')
    return render_template('home.html')