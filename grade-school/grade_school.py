import bisect

class School:
    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        sortedStudent = sorted((value, key) for (key, value) in self.students.items())
        return [student for (grade, student) in sortedStudent]
        

    def grade(self, grade_number):


        # return sorted(
        #     [
        #         student
        #         for student, grade in self.students.items()
        #         if grade == grade_number
        #     ]
        # )
school = School()
school.add_student(name="Franklin", grade=5)
school.add_student(name="Bradley", grade=5)
school.add_student(name="Jeff", grade=1)
expected = ["Bradley", "Franklin"]
print(school.grade(5))
