def InsertionSort(A):
    for i in range(1, len(A)):
        current_element = A[i]
        j = i - 1

        while j >= 0 and A[j] > current_element:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = current_element

input_list = input("Введите числа: ")
original_list = list(map(int, input_list.split()))

InsertionSort(original_list)

print("Output:", " ".join(map(str, original_list)))
