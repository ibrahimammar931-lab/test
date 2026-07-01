students = {
    "Alice": [15, 18, 14],
    "Bob": [10, 12, 11],
    "Charlie": [19, 17, 18]
}

class Student:
    def __init__(self, name, grades):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not all(isinstance(grade, (int, float)) for grade in grades):
            raise TypeError("Grades must be numeric")
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_results(self):
        avg = self.average()
        if avg >= 16:
            status = "Excellent"
        elif avg >= 10:
            status = "Passed"
        else:
            status = "Failed"
        print(f"{self.name}: Average = {avg:.2f} | {status}")


class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.name in self.students:
            raise ValueError("Student with the same name already exists")
        self.students[student.name] = student

    def display_results(self):
        print("Student Results")
        print("-" * 30)
        for student in self.students.values():
            student.display_results()


def main():
    db = StudentDatabase()
    db.add_student(Student("Alice", [15, 18, 14]))
    db.add_student(Student("Bob", [10, 12, 11]))
    db.add_student(Student("Charlie", [19, 17, 18]))
    db.display_results()

if __name__ == "__main__":
    main()