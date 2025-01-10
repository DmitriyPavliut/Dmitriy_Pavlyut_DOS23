from scripts.hello_world import *
from scripts.addition import *
from scripts.greet_user import *
from scripts.print_numbers import *
from scripts.user_age import *
from scripts.multiply_numbers import *
from scripts.first_letter import *
from scripts.square_number import *
from scripts.multiplication_table import *
from scripts.average import *

def main():
    while True:
        print("\n")
        print("Выберите скрипт для выполнения:")
        print("1. Привет, мир!")
        print("2. Результат 2+2")
        print("3. Приветствие пользователя")
        print("4. Числа от 1 до 10")
        print("5. Возраст пользователя")
        print("6. Произведение двух чисел")
        print("7. Первая буква слова")
        print("8. Квадрат числа")
        print("9. Таблица умножения на 5")
        print("10. Среднее арифметическое двух чисел")
        print("0. Выход")
        print("\n")

        choice = input("Введите номер (0-10): ")

        if choice == "1":
            print_hello_world()
        elif choice == "2":
            print_addition()
        elif choice == "3":
            greet_user()
        elif choice == "4":
            print_numbers()
        elif choice == "5":
            print_user_age()
        elif choice == "6":
            multiply_numbers()
        elif choice == "7":
            print_first_letter()
        elif choice == "8":
            print_square()
        elif choice == "9":
            print_multiplication_table()
        elif choice == "10":
            print_average()
        elif choice == "0":
            print("Выход из программы.")
            break  # Завершаем выполнение программы
        else:
            print("Неверный выбор! Пожалуйста, выберите номер от 0 до 10.")

if __name__ == "__main__":
    main()
