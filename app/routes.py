from app import app
from flask import render_template

@app.route('/')
def home():
    return "Homepage"

@app.route('/about')
def about():
    data = {
        'first_name': 'Darren',
        'last_name': 'Tran'
    }
    return data

@app.route('/contact')
def contact():
    return "Contact"