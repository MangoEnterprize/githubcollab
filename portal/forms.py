from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from portal.models import User

class RegisterForm(FlaskForm):

    # named specifically to validate username
    # def validate_username(self, username_to_check):
    #     # gets form info with .data
    #     user = User.query.filter_by(username=username_to_check.data).first()
    #     if user:
    #         raise ValidationError('Username already exists')
        
    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError('Email already exists')

    # username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    firstname = StringField(label="First Name", validators=[Length(min=3, max=30),DataRequired()])
    lastname = StringField(label="Last Name", validators=[Length(min=3, max=30),DataRequired()])
    email_address = EmailField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password1', validators=[Length(min=6, max=30), DataRequired()])
    password2 = PasswordField(label='Password2', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')



class LoginForm(FlaskForm):
    # username = StringField(label='Username', validators=[DataRequired()])
    email_address = EmailField(label='Email', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class ProfileForm(FlaskForm):
    # no validators needed, users can only submit via dropdowns
    major = StringField(label="Major")
    concentration = StringField(label="Major")
    gradmonth = StringField(label="Graduation Month")
    gradyear = StringField(label="Graduation Year")

class ExperienceForm(FlaskForm):
    # title, desc, month, year
    title = StringField(label="Title")
    desc = StringField(label="Desc")
    company = StringField(label="Company")
    month = StringField(label="Month")
    year = IntegerField(label="Year")