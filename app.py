from flask import Flask, render_template
app = Flask(__name__)

@app.route("/alvinalaphat.git", methods=['GET','POST'])
def hello():
    return render_template("dashboard.html")

@app.route("/")
def dash():
    return render_template("dashboard.html")