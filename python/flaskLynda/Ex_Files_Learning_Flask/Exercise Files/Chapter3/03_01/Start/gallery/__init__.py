from flask import Flask
from gallery.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

import gallery.views, gallery.models

db.create_all()

