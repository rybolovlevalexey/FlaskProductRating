from flask import Flask, render_template
from product_rating_app.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
