# save this as app.py
from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World! this is my fisrt flsk app"
"""
@app.route('/hello/')
def hello():
    return 'this is my first home page'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
"""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('test.html', name=name)

