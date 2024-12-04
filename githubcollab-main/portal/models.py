from portal import db, bcrypt, login_manager
from flask_login import UserMixin


# gets id of current session user, allows you to access current_user variable inside routes 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# usermixin has premade auth function
class User(db.Model, UserMixin):

    # Validate by unique username
    # id is needed
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(length=30), nullable=False, unique=False)
    lastname = db.Column(db.String(length=30), nullable=False, unique=False)
    email_address=db.Column(db.String(length=50), nullable=True, unique=True)
    #store passwords as hash
    password_hash= db.Column(db.String(length=60), nullable=False)

    #profile details
    major=db.Column(db.String(length=30), nullable=True)
    concentration=db.Column(db.String(length=30), nullable=True)
    gradmonth=db.Column(db.Integer(), nullable=True)
    gradyear=db.Column(db.Integer(), nullable=True)
    
    #define relationship between models
    #not stored as a column
    # exp = db.relationship('Experience', backref='user_id', lazy=True)

    # additional attribute accessible from each instance
    @property
    def password(self):
        return self.password
    
    # set password before creating user insance
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
            

# store job experience and volunteer experience
class Experience(db.Model):
    # title, desc, company, date
    id = db.Column(db.Integer(),  primary_key=True)
    title=db.Column(db.String(length=30), nullable=False)
    company=db.Column(db.String(length=30), nullable=True)
    desc=db.Column(db.String(length=250), nullable=True)

    monthstart=db.Column(db.String(length=30), nullable=True)
    yearstart=db.Column(db.Integer(), nullable=True)

    monthend=db.Column(db.String(length=30), nullable=True)
    yearend=db.Column(db.Integer(), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # additional attribute accessible from each instance
    @property
    def format(self):
        body = [self.title, self.desc, self.monthstart, self.yearstart, self.monthend, self.yearend]
        return body
    

    def __repr__(self):
        nl = "\n"
        # print(f'Experience 1: {self.title}{nl}{self.desc}{nl}')
        return f'{self.title}{nl}{self.desc}{nl}'