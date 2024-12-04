from portal import app
from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from portal.models import  User, Experience
from portal.forms import RegisterForm, LoginForm, ProfileForm, ExperienceForm
from portal import db
from flask_login import login_user, logout_user, login_required, current_user
import calendar

# this is root url, can handle mulriple decorators
@app.route('/') 
@app.route('/home')
def home_page():
    
    return render_template('home.html')

# TODO:needs to take logged in username
@app.route('/about')
def about_page():
    return f'<h1>This is the about page of user</h1>'

@app.route('/scholarship')
def scholarship_page():
    return render_template('scholarship.html')


@app.route('/jobs')
# @login_required
def portal_page():
    # Items has been removed
    # items = Item.query.all()
    return render_template('home.html')

@app.route('/tutoring')
def tutoring_page():
    return render_template('tutoring.html')

@app.route('/job')
def jobs_page():
    return render_template('job.html')

@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile_page():
    majors = ['Computer Science', 'English', 'Business Administration', 'Psychology', 'Biology', 'Engineering', 'Art', 'History', 'Mathematics']
    years = [ 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    months = list(calendar.month_name)[1:]

    form = ProfileForm()
    form2 = ExperienceForm()

    if not current_user.is_authenticated:
        flash(f'Required login for this page is currently disabled. For testing purposes, we are using maddie as the user. Work in progress', category='success')
        user = User.query.filter_by(email_address="mbrow378@uncc.edu").first()
    else:
        user = User.query.filter_by(id=current_user.id).first()
    #   User.query.get_or_404(current_user.id)

    # distinguish by which form is submitted
    if form2.validate_on_submit() and form2.submit2.data:
        print(request.form.get('monthstart'))
        print(request.form.get('yearstart'))
        print(request.form.get('monthend'))
        print(request.form.get('yearend'))
        # create new job experience object
        #use request.form.get to get form items based on select name
        new_exp = Experience(title=form2.title.data,
                            desc=form2.desc.data,
                            user_id = user.id,
                            monthstart = request.form.get('monthstart'),
                            yearstart = request.form.get('yearstart'),
                            monthend = request.form.get('monthend'),
                            yearend = request.form.get('yearend')
                            )
        db.session.add(new_exp)
        db.session.commit()

        flash(f'New experience added to profile', category='success')
        # return redirect(url_for('dashboard_page'))

    # Update information
    if form.validate_on_submit() and form.submit.data:
        user.major=form.major.data
        # user.concentration=form.concentration.data
        # user.gradmonth=form.gradmonth.data
        # user.gradyear=form.gradyear.data
        
        db.session.commit()

        flash(f'Profile updated successfully', category='success')
        # return redirect(url_for('dashboard_page'))
    

    # Errors
    if form.errors: #if no errors from validation
        for error in form.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')

    if form2.errors: #if no errors from validation
        for error in form2.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')
    
    return render_template('profile.html', form=form, majors=majors, form2=form2, years=years, months=months, user=user)

# User must be logged in to access dashboard
@app.route('/dashboard')
# @login_required
def dashboard_page():

    if not current_user.is_authenticated:
        flash(f'Required login for this page is currently disabled. For testing purposes, we are using maddie as the user', category='success')
        user = User.query.filter_by(email_address="mbrow378@uncc.edu").first()
        experiences = (Experience.query.filter_by(user_id=user.id)).all()
    else:
        user = User.query.filter_by(id=current_user.id).first()
        experiences = (Experience.query.filter_by(user_id=current_user.id)).all()
        # loop through experiences calling the formatting function
        experiences = [x.format for x in experiences]

    return render_template('dashboard.html', experiences=experiences, user=user)


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
            flash(f'Success, logged in as: {attemptedUser.firstname}', category='success')
            return redirect(url_for('dashboard_page'))
        else:
            flash("Failed login", category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You logged out", category='info')
    return render_template('home.html')