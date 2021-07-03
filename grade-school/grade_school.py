

class School:
    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        sortedStudent = sorted((value, key) for (key, value) in self.students.items())
        return [student for (grade, student) in sortedStudent]
        
    def grade(self, grade_number):
        return sorted(
            [
                student
                for student, grade in self.students.items()
                if grade == grade_number
            ]
        )


school = School()
school.add_student(name="Peter", grade=2)
school.add_student(name="Anna", grade=1)
school.add_student(name="Barb", grade=1)
school.add_student(name="Zoe", grade=2)
school.add_student(name="Alex", grade=2)
school.add_student(name="Jim", grade=3)
school.add_student(name="Charlie", grade=1)
expected = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
print(school.roster())