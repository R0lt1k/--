def align_strings(strings):
    max_length = max(len(s) for s in strings)

    print(max_length)

    for s in strings:
        padding = max_length - len(s)
        stars = '*' * padding
        print(stars + s)

M = int(input("Введите количество строк M: "))
input_strings = [input() for _ in range(M)]

align_strings(input_strings)
