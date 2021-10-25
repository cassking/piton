import sys

from flask import Flask, render_template
app = Flask(__name__)

num_clicks = 0
number = 9

@app.route("/")
def index():
    return render_template('index.html', num_clicks=num_clicks)
    # print('This is standard output', file=sys.stdout)
# print(number, file=sys.stdout)
@app.route("/about")
def about():
    return "<p>About this thing</p>"
