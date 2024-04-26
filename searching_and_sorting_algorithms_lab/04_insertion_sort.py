def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i, 0, - 1):
            num1 = array[j]
            num2 = array[j - 1]
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


array = [int(ch) for ch in input().split(' ')]
print(*insertion_sort(array), sep=' ')