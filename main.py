from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import csv

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy routes for demonstration
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if email == "admin@example.com" and password == "password":
        session['email'] = email
        return redirect(url_for('dashboard'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
