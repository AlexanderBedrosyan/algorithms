def selection_sort(arr):
    for i in range(len(arr)):
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[min_element] > arr[j]:
                min_element = j
        element = arr.pop(min_element)
        arr.insert(i, element)

    return arr


nums = [int(ch) for ch in input().split(' ')]
print(*selection_sort(nums), sep=' ')
