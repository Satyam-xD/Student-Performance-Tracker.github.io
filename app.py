from flask import Flask, render_template, request, redirect, url_for
from student_tracker import StudentTracker

app = Flask(__name__)
tracker = StudentTracker()  # Initialize the StudentTracker

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        tracker.add_student(name, roll_number)
        return redirect(url_for('index', message="Student added successfully!"))
    return render_template('add_student.html')

@app.route('/view_students')
def view_students():
    return render_template('view_students.html', students=tracker.students)

@app.route('/add_grade/<roll_number>', methods=['GET', 'POST'])
def add_grade(roll_number):
    student = tracker.view_student(roll_number)
    if not student:
        return "Student not found", 404
    if request.method == 'POST':
        subject = request.form['subject']
        grade = request.form['grade']
        if subject and grade.isdigit() and 0 <= int(grade) <= 100:
            tracker.add_grades(roll_number, subject, int(grade))
            return redirect(url_for('view_student', roll_number=roll_number))
        else:
            return "Invalid grade entry. Please enter a grade between 0 and 100.", 400
    return render_template('add_grade.html', student=student)

@app.route('/view_student/<roll_number>')
def view_student(roll_number):
    student = tracker.view_student(roll_number)
    if not student:
        return "Student not found", 404
    return render_template('view_student.html', student=student)

@app.route('/class_average')
def class_average():
    average = tracker.calculate_class_average()
    return render_template('class_average.html', average=average)

if __name__ == '__main__':
    app.run(debug=True)
