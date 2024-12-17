from classes.сircle import *
from classes.bankaccount import *
from classes.student import *
from classes.book import *
from classes.car import *

#Circle
circle1 = Circle(5, "красный")
circle2 = Circle(10, "синий")

print("Круг 1:")
print(f"Цвет: {circle1.color}, Площадь: {circle1.calculate_area():.2f}, Длина окружности: {circle1.calculate_circumference():.2f}")
print("Круг 2:")
print(f"Цвет: {circle2.color}, Площадь: {circle2.calculate_area():.2f}, Длина окружности: {circle2.calculate_circumference():.2f}")

#BankAccount
account1 = BankAccount("123456", "Иван Иванов", 1000)
account2 = BankAccount("654321", "Мария Смирнова", 5000)

print("\nБанковский счет 1:")
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)

print("\nБанковский счет 2:")
account2.withdraw(1000)
account2.deposit(2000)


# Student
student1 = Student("Анна Петрова", 19, [5, 4, 5, 5, 4])
student2 = Student("Алексей Смирнов", 20, [3, 4, 3, 4, 3])

print("\nСтудент 1:")
print(f"Имя: {student1.name}, Средний балл: {student1.calculate_average():.2f}, Статус: {student1.determine_status()}")

print("Студент 2:")
print(f"Имя: {student2.name}, Средний балл: {student2.calculate_average():.2f}, Статус: {student2.determine_status()}")


# Book
book1 = Book("Война и мир", "Лев Толстой", 1869)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 1866)

print("\nКнига 1:")
print(book1.get_info())
book1.set_year(1870)
print(f"Обновлённый год издания: {book1.get_info()}")

print("Книга 2:")
print(book2.get_info())


# Car
car1 = Car("Toyota", "Camry", "чёрный", 2020)
car2 = Car("BMW", "X5", "белый", 2018)

print("\nАвтомобиль 1:")
print(car1.get_info())
car1.set_color("синий")
print(f"Обновлённый цвет: {car1.get_info()}")

print("Автомобиль 2:")
print(car2.get_info())