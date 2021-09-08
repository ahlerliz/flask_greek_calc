# Put your app in her
from flask import Flask, request
import operations

app = Flask(__name__)

#Question: what is wrong
# @app.get("/add?a=<int:numA>&b=<int:numB>") #'/add?a=2&b=2')
# def add(a,b):
#     a =  request.args["a"]
#     b = request.args["b"]
#     return operations.add(a, b)

@app.get("/add") #'/add?a=2&b=2')
def add():
    a =  int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a, b))

@app.get("/sub")
def sub():
    a =  int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a, b))


@app.get("/mult")
def mult():
    a =  int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a, b))

@app.get("/div")
def div():
    a =  int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.div(a, b))