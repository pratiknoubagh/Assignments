from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


employee_names = []


@app.route('/')
def index():
    return render_template('index.html', employee_names=employee_names)


@app.route('/add_employee', methods=['POST'])
def add_employee():
   
    employee_name = request.form.get('employee_name')

    if employee_name:
        employee_names.append(employee_name)

    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
