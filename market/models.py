from market import db, bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# usermixin has premade auth function
class User(db.Model, UserMixin):
    # id is needed
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address=db.Column(db.String(length=50), nullable=True, unique=True)
    #store passwords as hash
    password_hash= db.Column(db.String(length=60), nullable=False)
    budget=db.Column(db.Integer(), nullable=False, default=1000)

    #define relationship between models
    #not stored as a column
    items = db.relationship('Item', backref='owned_user', lazy=True)

    # additional attribute accessible form each instance
    @property
    def password(self):
        return self.password
    
    # set password before creating user insance
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
            

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=4), nullable=False, unique=True)
    desc = db.Column(db.String(1024), nullable=False)

    #foreign key
    owner=db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item{self.name}'

