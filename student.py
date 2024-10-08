class Student:
    def __init__(self, name, roll_number, grades=None):
        self.name = name
        self.roll_number = roll_number
        self.grades = grades if grades is not None else {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, grades={self.grades})"
