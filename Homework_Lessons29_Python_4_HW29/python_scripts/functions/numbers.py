def sort_descending(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    print("Отсортированный список:", sorted_numbers)

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    print("Медиана:", median)
