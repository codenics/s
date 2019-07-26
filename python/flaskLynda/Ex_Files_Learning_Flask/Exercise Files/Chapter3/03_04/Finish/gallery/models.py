from gallery import app, db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db.create_all()

class LoginUser(db.Model, UserMixin):
       __tablename__ = 'user'

       email = db.Column(db.String, primary_key=True)
       authenticated = db.Column(db.Boolean, default=False)
       pw_hash = db.Column(db.String)

       def is_active(self):
            return True

       def get_id(self):
            return self.email

       def is_authenticated(self):
            return self.authenticated

       def is_anonymous(self):
            return False

       def set_password(self, password):
           self.pw_hash = generate_password_hash(password)

       def check_password(self, password):
           return check_password_hash(self.pw_hash, password)