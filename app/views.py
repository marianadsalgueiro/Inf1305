# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/forgot-password.html')
def forgot_password():
    return render_template("forgot-password.html")

@app.route('/tables.html')
def tables():
    return render_template("tables.html")