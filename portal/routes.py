from portal import app
from flask import request, render_template, redirect, url_for, flash, get_flashed_messages
from portal.models import User, Experience
from portal.forms import RegisterForm, LoginForm, ProfileForm, ExperienceForm
from portal import db
from flask_login import login_user, logout_user, login_required, current_user
import calendar
import pandas as pd  # Import pandas for reading CSV files

# Root URL
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# About page
@app.route('/about')
def about_page():
    return f'<h1>This is the about page of user</h1>'

# Scholarship page with dynamic CSV data
@app.route('/scholarship')
def scholarship_page():
    # Define the path to your CSV file
    csv_path = "portal/templates/data folder/example-scholarships.csv"

    # Read the CSV file using pandas
    try:
        scholarships_data = pd.read_csv(csv_path)
        scholarships = scholarships_data.to_dict(orient='records')  # Convert to list of dictionaries
    except Exception as e:
        scholarships = []  # Default to an empty list if there's an issue with the file
        flash(f"Error loading scholarships: {e}", category='danger')

    # Render the scholarships page with the data
    return render_template('scholarship.html', scholarships=scholarships)

@app.route('/jobs')
def portal_page():
    return render_template('home.html')

@app.route('/tutoring')
def tutoring_page():
    return render_template('tutoring.html')

@app.route('/job')
def jobs_page():
    return render_template('job.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    majors = ['Computer Science', 'English', 'Business Administration', 'Psychology', 'Biology', 'Engineering', 'Art', 'History', 'Mathematics']
    years = list(range(2013, 2025))
    months = list(calendar.month_name)[1:]

    form = ProfileForm()
    form2 = ExperienceForm()
    user = User.query.filter_by(id=current_user.id).first()

    if form2.validate_on_submit() and form2.submit2.data:
        new_exp = Experience(title=form2.title.data, desc=form2.desc.data, user_id=user.id)
        db.session.add(new_exp)
        db.session.commit()
        flash(f'New experience added to profile', category='success')

    if form.validate_on_submit() and form.submit.data:
        user.major = form.major.data
        db.session.commit()
        flash(f'Profile updated successfully', category='success')

    if form.errors:
        for error in form.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')

    if form2.errors:
        for error in form2.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')
    
    return render_template('profile.html', form=form, majors=majors, form2=form2, years=years, months=months)

@app.route('/dashboard')
@login_required
def dashboard_page():
    experiences = Experience.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', experiences=experiences)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email_address=form.email_address.data,
            password=form.password1.data
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created, logged in as: {user_to_create.firstname}', category='success')
        return redirect(url_for('home_page'))

    if form.errors:
        for error in form.errors.values():
            flash(f'Error during submission: {error[0]}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success, logged in as: {attempted_user.firstname}', category='success')
            return redirect(url_for('dashboard_page'))
        else:
            flash("Failed login", category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You logged out", category='info')
    return render_template('home.html')
