class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # список оценок

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def determine_status(self):
        avg = self.calculate_average()
        if avg >= 4.5:
            return "Отличник"
        elif avg >= 3.5:
            return "Хорошист"
        else:
            return "Троечник"