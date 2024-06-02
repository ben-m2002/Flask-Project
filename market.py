from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("Home.html")

# basically this means that the username can be appended to this route, and we can handle that dynamically
@app.route('/about/<username>')
def about(username):
    return f'<h1>This is the about page of {username}</h1>'

