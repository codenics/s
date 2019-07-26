from gallery import app, db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db.create_all()

class Appuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    images = db.relationship("Appimage", backref="appuser", lazy=True)

    def __repr__(self):
        return '<Appuser %r>' % self.email

class Appimage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    URL = db.Column(db.String(120), unique=True, nullable=False)
    appuser_id = db.Column(db.Integer, db.ForeignKey('appuser.id'))
    
    def __repr__(self):
        return '<Appimage %r: %s>' % (self.URL,self.appuser.email)

