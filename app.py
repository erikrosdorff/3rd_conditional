from flask import Flask

app = Flask(__name__)

@app.route("/")
def calculate():
    return "I am a function"