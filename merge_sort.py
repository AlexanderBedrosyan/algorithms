def merge_arrays(left_array, right_array):
    result = []
    left_ind = 0
    right_ind = 0

    while left_ind < len(left_array) and right_ind < len(right_array):
        if left_array[left_ind] < right_array[right_ind]:
            result.append(left_array[left_ind])
            left_ind += 1

        else:
            result.append(right_array[right_ind])
            right_ind += 1

    for ind in range(left_ind, len(left_array)):
        result.append(left_array[ind])

    for ind in range(right_ind, len(right_array)):
        result.append(right_array[ind])

    return result


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(ch) for ch in input().split(' ')]
print(*merge_sort(nums), sep=' ')