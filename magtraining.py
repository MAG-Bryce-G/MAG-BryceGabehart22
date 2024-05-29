from flask import Flask
import gunicorn
app = Flask(__name__)


@app.route('/')
def training():
    #construct your message here
    message = """
    <html>
    <body>
    <h1>Training 22</h1>
    <p>Hi, my name is Bryce.</p>
    </body>
    </html>
    """
    return message
