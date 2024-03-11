def bubble_sort(array):
    is_sorted = False
    for i in range(len(array) - 1):
        is_sorted = True
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False

        if is_sorted:
            return array
    return array


array = [int(ch) for ch in input().split()]
print(*bubble_sort(array), sep=' ')