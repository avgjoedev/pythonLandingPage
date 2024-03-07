from flask import Flask

app = Flask(__name__)

username = "Its me, Joe"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user")
def user():
    return f"Who are you ? {username}"

@app.route("/dtw")
def user_input():
    name = input("What is your name?")
    return name