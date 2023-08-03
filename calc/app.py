# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route('/add')
def addition():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = add(a, b)
    return str(result)
    
@app.route('/sub')
def subtraction():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = div(a, b)
    return str(result)

@app.route('/math/<operation>')
def math_operations(operation):
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    if operation == 'add':
        result = add(a, b)
    elif operation == 'sub':
        result = sub(a, b)
    elif operation == 'mult':
        result = mult(a, b)
    elif operation == 'div':
        result = div(a, b)
    else:
        return "Invalid operation"
    return str(result)

if __name__ == '__main__':
    app.run()