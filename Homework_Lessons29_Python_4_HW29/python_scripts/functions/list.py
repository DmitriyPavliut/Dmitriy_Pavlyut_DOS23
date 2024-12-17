def common_elements(list1, list2):
    result = list(set(list1) & set(list2))
    print("Общие элементы:", result)


def unique_common_elements(list1, list2):
    common = set(list1) & set(list2)
    unique = list(set(common))
    print("Уникальные общие элементы:", unique)
