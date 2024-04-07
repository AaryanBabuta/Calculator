from flask import Flask, request, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route to the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = perform_operation(num1, num2, operation,)
        return render_template('result.html', num1=num1, num2=num2, operation=operation, result=result)
    return render_template('index.html')

# Function to perform arithmetic operation
def perform_operation(num1, num2, operation,):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
