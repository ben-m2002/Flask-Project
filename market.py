from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to the market!!!</h-1>"

@app.route('/about')
def about():
    return "<h1>This is the about page</h1>"

