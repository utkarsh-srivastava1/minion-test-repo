import webbrowser
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def hello():
    return 'Hello World'

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    return a + b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    return a * b

def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    return a ** b

def modulo(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a % b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both inputs must be numbers')
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b

@app.route('/'
        , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            operation = request.form['operation']
            if operation == 'add':
                result = add(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'power':
                result = power(a, b)
            elif operation == 'modulo':
                result = modulo(a, b)
            elif operation == 'divide':
                result = divide(a, b)
            else:
                return 'Invalid operation'
            return jsonify({'result': result})
        except Exception as e:
            return str(e)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)