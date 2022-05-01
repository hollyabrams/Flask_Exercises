from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Says welcome"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """Says welcome home"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Says welcome back"""
    return "welcome back"