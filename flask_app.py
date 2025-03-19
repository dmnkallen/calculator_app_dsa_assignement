from flask import Flask, render_template, request
from circle import Circle  # Importing the Circle class
from helper import perform_calculation, convert_to_float  

app = Flask(__name__)  # Create the instance of the Flask class

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        if operation not in ['add', 'subtract', 'divide', 'multiply']:
            return render_template('calculator.html',
                                   printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle_calculator():
    if request.method == 'POST':
        try:
            radius = float(request.form['radius'])
            circle = Circle(radius)
            area = circle.area()
            perimeter = circle.perimeter()
            return render_template('circle_calculator.html', area=area, perimeter=perimeter, radius=radius)
        except ValueError:
            return render_template('circle_calculator.html', error="Invalid input. Please enter a positive number.")

    return render_template('circle_calculator.html')

if __name__ == '__main__':
    app.run(debug=True)

