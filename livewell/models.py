from datetime import datetime
from livewell import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False) #description
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # House stuff
    rent = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, nullable=False)
    address = db.Column(db.String(140), nullable=False)
    gender_filter = db.Column(db.Integer, nullable=False)
    pet_filter = db.Column(db.Boolean, nullable=False)
    picture = db.Column(db.String(140), nullable=True) # link to file hosting website
    #images = db.relationship('Image', backref='post', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.rent}', '{self.date_posted}')"