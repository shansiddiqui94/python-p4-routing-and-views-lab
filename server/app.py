#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':  #alt way of starting py
    app.run(port=5555, debug=True)

@app.route("/") #setting up my route
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200 #returning a status code


@app.route('/print/<string:parameter>') # you need to pass the datatype in the parameter 
def print_string(parameter):
    print(parameter)  # Printing the parameter in the console
    return parameter, 200
# <parameter>: This part of the route acts as a placeholder for any value that comes after /print/. It tells Flask to capture whatever value is present at this position in the URL and pass it as an argument to the corresponding view function.

@app.route('/count/<int:parameter>') 
def count(parameter):
    result = ''
    for num in range(parameter):
        result += str(num) + '\n'
        
    return result, 200



@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return  str(num1 + num2), 200
    elif operation == '-':
        return  str(num1 - num2), 200   
    elif operation == '*':
        return  str(num1 * num2), 200
    elif operation == 'div':
        return  str(num1 / num2), 200
    elif operation == '%':
        return  str(num1 % num2), 200
    else:
        return f'invalid operator: [operation]', 404
    
