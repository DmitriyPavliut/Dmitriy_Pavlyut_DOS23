import string

def analyze_string(input_string):
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    digit_count = sum(1 for char in input_string if char.isdigit())
    punctuation_count = sum(1 for char in input_string if char in string.punctuation)

    print(f"Количество букв в верхнем регистре: {upper_count}")
    print(f"Количество букв в нижнем регистре: {lower_count}")
    print(f"Количество цифр: {digit_count}")
    print(f"Количество символов пунктуации: {punctuation_count}")


def common_characters(str1, str2):
    result = sorted(set(str1) & set(str2))
    print("Общие символы:", ''.join(result))


def replace_vowels(input_string):
    vowels = "AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя"
    result = ''.join("-" if char in vowels else char for char in input_string)
    print("Результат:", result)

