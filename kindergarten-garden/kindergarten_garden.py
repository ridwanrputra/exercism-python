KIDS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=KIDS):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        idx = self.students.index(student) * 2
        return list(
            map(
                PLANTS.get,
                (
                    self.diagram[0][idx],
                    self.diagram[0][idx + 1],
                    self.diagram[1][idx],
                    self.diagram[1][idx + 1],
                ),
            )
        )
