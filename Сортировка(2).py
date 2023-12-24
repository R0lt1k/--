def find_closest_numbers(lst):
    sorted_lst = sorted(lst)

    min_difference = float('inf')
    closest_pair = None

    for i in range(len(sorted_lst) - 1):
        difference = sorted_lst[i + 1] - sorted_lst[i]

        if difference < min_difference:
            min_difference = difference
            closest_pair = [sorted_lst[i], sorted_lst[i + 1]]

    return closest_pair

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

result = find_closest_numbers(numbers)
print(*result)
##AAAAAA
