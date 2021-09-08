from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def first_welcome():
    return ("Welcome!")

@app.get("/welcome/home")
def welcome_home():
    return ("Welcome Home!")

@app.get("/welcome/back")
def welcome_back():
    return ("Welcome Back!")
