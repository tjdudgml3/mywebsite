from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("make_page.html")


@app.route('/welcome/')
def hello():
    return 'wel'


@app.route('/welcome/<das>/')
def welcome1(das):
    print(das)
    return f'wel{das}'

app.run()