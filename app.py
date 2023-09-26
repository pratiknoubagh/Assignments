from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list to store employee names
employee_names = []


@app.route('/')
def index():
    return render_template('index.html', employee_names=employee_names)


@app.route('/add_employee', methods=['POST'])
def add_employee():
    # Get the employee name from the form
    employee_name = request.form.get('employee_name')

    # Add the employee name to the list
    if employee_name:
        employee_names.append(employee_name)

    # Redirect back to the index page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
