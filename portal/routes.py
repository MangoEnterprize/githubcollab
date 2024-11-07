from portal import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from portal.models import  User
from portal.forms import RegisterForm, LoginForm, ProfileForm
from portal import db
from flask_login import login_user, logout_user, login_required, current_user

# this is root url, can handle mulriple decorators
@app.route('/') 
@app.route('/home')
def home_page():
    return render_template('home.html')

# dynamic route takes username
@app.route('/about')
def about_page(username):
    return f'<h1>This is the about page of username</h1>'

@app.route('/jobs')
@login_required
def portal_page():
    # Items has been removed
    # items = Item.query.all()
    return render_template('home.html')

@app.route('/job')
def jobs_page():
    return render_template('job.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_page():

    form = ProfileForm()
    user = User.query.filter_by(id=current_user.id).first()
    #   User.query.get_or_404(current_user.id)

    # Update information
    if form.validate_on_submit():
        user.major=form.major.data
        user.concentration=form.concentration.data
        user.gradmonth=form.gradmonth.data
        user.gradyear=form.gradyear.data
        
        db.session.commit()

        flash(f'Profile updated successfully', category='success')
        return redirect(url_for('dashboard_page'))
    
    if form.errors: #if no errors from validation
        for error in form.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')
    
    return render_template('profile.html', form=form)

# User must be logged in to access dashboard
@app.route('/dashboard')
@login_required
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(firstname=form.firstname.data,
                              lastname=form.lastname.data, 
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        # login registered user
        login_user(user_to_create)
        flash(f'Account created, logged as: {user_to_create.firstname}', category='success')
            

        return redirect(url_for('home_page'))
    
    if form.errors: #if no errors from validation
        for error in form.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # verify user exists and password correct
        attemptedUser = User.query.filter_by(email_address=form.email_address.data).first()
        if attemptedUser and attemptedUser.check_password_correction(
            attempted_password=form.password.data
        ): 
            login_user(attemptedUser)
            flash(f'Success, login as: {attemptedUser.firstname}', category='success')
            return redirect(url_for('portal_page'))
        else:
            flash("Failed login", category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You logged out", category='info')
    return render_template('home.html')