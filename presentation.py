import logic
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    students = logic.view_students()
    return render_template('index.html', students=students, message=None)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = int(request.form['age'])
    course = request.form['course']
    
    message = logic.add_student(name, age, course)
    students = logic.view_students()
    return render_template('index.html', students=students, message=message)

@app.route('/delete/<int:std_id>')
def delete(std_id):
    message = logic.remove_student(std_id)
    students = logic.view_students()
    return render_template('index.html', students=students, message=message)

if __name__ == "__main__":
    app.run(debug=True)
