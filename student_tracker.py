import json
from student import Student

class StudentTracker:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, 'r') as f:
                student_data = json.load(f)
                return [Student(**data) for data in student_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump([student.__dict__ for student in self.students], f)

    def add_student(self, name, roll_number):
        new_student = Student(name, roll_number)
        self.students.append(new_student)
        self.save_students()

    def add_grades(self, roll_number, subject, grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.add_grade(subject, grade)
                self.save_students()
                break

    def view_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def calculate_class_average(self):
        if len(self.students) == 0:
            return 0
        total = 0
        count = 0
        for student in self.students:
            total += student.calculate_average()
            count += 1
        return total / count
