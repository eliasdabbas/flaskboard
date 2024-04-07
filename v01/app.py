from flask import Flask

from dashboard1 import app as app1
from dashboard2 import app as app2
from home import app as app_home

app = Flask(__name__)

app_home.init_app(app)
app1.init_app(app)
app2.init_app(app)