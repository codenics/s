import werkzeug.security
from flask import render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from gallery import app, db, models

Bootstrap(app)

@app.route('/images')
def images():
    images = models.Appimage.query.all()
    return render_template('images.html', images=images)

