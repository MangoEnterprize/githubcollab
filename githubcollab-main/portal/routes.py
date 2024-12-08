from portal import app
from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from portal.models import  User, Experience
from portal.forms import RegisterForm, LoginForm, ProfileForm, ExperienceForm
from portal import db
from flask_login import login_user, logout_user, login_required, current_user
import calendar
from markupsafe import Markup

import csv  # Built-in CSV module
import pandas as pd  # Optional: For advanced CSV handling


# Using built-in csv module

# Using pandas (optional, for larger datasets or complex manipulation)
@app.route('/csv')
def fetch_csv_pandas():
    df = pd.read_csv('C:/Users/Lillian/githubcollab/githubcollab-main/portal/static/updated_scholarships.csv')
    scholarships = df.to_dict(orient='records')

    # Pass the scholarships data to the template
    return render_template('test.html', scholarships=scholarships)


# If user is not logged in, user default user maddie
def getUser():
    if not current_user.is_authenticated:
        flash(f'Required login for this page is currently disabled. Using maddie as default', category='success')
        user = User.query.filter_by(email_address="mbrow378@uncc.edu").first()
    else:
        user = User.query.filter_by(id=current_user.id).first()
    return user

# this is root url, can handle mulriple decorators
@app.route('/') 
@app.route('/home')
def home_page():
    
    return render_template('home.html')

@app.route('/scholarship')
def scholarship_page():
    df = pd.read_csv('C:/Users/Lillian/githubcollab/githubcollab-main/portal/static/updated_scholarships.csv')
    scholarships = df.to_dict(orient='records')

    return render_template('scholarship.html', scholarships=scholarships)


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


def updateMsg():
    flash(f'Profile updated successfully', category='success')
    flash(Markup('See changes in <a href="/dashboard">Dashboard</a>'),category='success')
    db.session.commit()

@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile_page():
    # TODO: edit experiences and add multiple experiences at once
    majors = ['Computer Science', 'English', 'Business Administration', 'Psychology', 'Biology', 'Engineering', 'Art', 'History', 'Mathematics']
    years = [ 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    months = list(calendar.month_name)[1:]
    concentrations = ['Software Engineering', 'Systems', 'AI and Game Development']

    form = ProfileForm()
    form2 = ExperienceForm()
    form3 = ExperienceForm()

    # set user to maddie if not logged in
    user = getUser()
    #   User.query.get_or_404(current_user.id)

    #Job experience submission
    if form2.validate_on_submit() and form2.submit2.data:
        #use request.form.get to get form select items based on name attribute
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

        if form2.errors: #if no errors from validation
            for error in form2.errors.values():
                flash(f'Error during submission: {error[0]}', category='danger')
        # return redirect(url_for('dashboard_page'))

    # Add volunteer exp
    if form3.validate_on_submit() and form3.submit3.data:
        #use request.form.get to get form items based on select name
        new_exp = Experience(title=form3.title.data,
                            desc=form3.desc.data,
                            user_id = user.id,
                            company = form3.company.data,
                            monthstart = request.form.get('volunteermonth'),
                            yearstart = request.form.get('volunteeryear'),
                            )
        db.session.add(new_exp)
        updateMsg()

        if form3.errors: #if no errors from validation
            for error in form3.errors.values():
                flash(f'Error during submission: {error[0]}', category='danger')

    # Update information
    elif form.validate_on_submit() and form.submit.data:
        user.major=form.major.data  
        updateMsg()
        
        # Errors
        if form.errors: #if no errors from validation
            for error in form.errors.values():
                flash(f'Error during submission: {error[0]}', category='danger')
    
    elif request.method == 'POST' and 'Concentration' in request.form:
        user.concentration = request.form['Concentration']
        updateMsg()

    elif request.method == 'POST' and 'gradyear' in request.form or 'gradmonth' in request.form:
        user.gradyear = request.form['gradyear']
        user.gradmonth = request.form['gradmonth']
        updateMsg()
    
    return render_template('profile.html', form=form, majors=majors, form2=form2, years=years, months=months, user=user, concentrations=concentrations, form3=form3)

# User must be logged in to access dashboard
@app.route('/dashboard')
# @login_required
def dashboard_page():

    user = getUser()
    experiences = (Experience.query.filter_by(user_id=user.id)).all()
    
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