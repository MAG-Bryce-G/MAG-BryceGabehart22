from flask import Flask
from flask import render_template
import gunicorn
app = Flask(__name__)


@app.route('/')
def training():
    #construct your message here
    render_template("index.html")
    return 200
