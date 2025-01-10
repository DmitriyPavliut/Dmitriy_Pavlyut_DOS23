def print_first_letter():
    word = input("Введите слово: ")
    if word:
        print(f"Первая буква: {word[0]}")
    else:
        print("Вы ничего не ввели!")
