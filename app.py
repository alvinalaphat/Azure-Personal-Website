from flask import Flask
app = Flask(__name__)

@app.route("/alvinalaphat.git")
def hello():
    return "Welcome to Alvin's Personal Website!"
