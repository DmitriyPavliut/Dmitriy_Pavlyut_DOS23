def check_uniqueness(tpl):
    if len(tpl) == len(set(tpl)):
        print("Все элементы уникальны")
    else:
        print("Есть повторяющиеся элементы")


