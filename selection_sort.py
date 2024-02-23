my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)

for i in range(n-1):
    min_index = i

    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)


# Second solution
nums = [64, 34, 25, 5, 22, 11, 90, 12]

for idx in range(len(nums)):
    min_idx = idx
    for curr_idx in range(idx + 1, len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            min_idx = curr_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(nums)