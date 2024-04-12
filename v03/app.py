from dashboard1 import app as app1
from dashboard2 import app as app2
from flask import Flask, render_template
from home import app as app_home

app = Flask(__name__)

app_home.init_app(app)
app1.init_app(app)
app2.init_app(app)


@app.route("/")
def index():
    return render_template("base.html", app=app_home)


@app.route("/dashboard1/")
@app.route("/dashboard1/<country>")
def dashboard1(country=None):
    if not country:
        country = ""
    return render_template("base.html", app=app1, country=country)


@app.route("/dashboard2/")
def dashboard2():
    return render_template("base.html", app=app2)
