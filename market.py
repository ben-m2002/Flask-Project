from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/home")
def home_page():
    return render_template("Home.html")


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template("market.html", items=items)


# basically this means that the username can be appended to this route, and we can handle that dynamically
@app.route('/about/<username>')
def about(username):
    return f'<h1>This is the about page of {username}</h1>'
