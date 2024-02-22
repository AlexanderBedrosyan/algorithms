# AVG Time Complexity O(log(n))

def binary_search(nums, target):
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_ind = (left_index + right_index) // 2
        element = nums[mid_ind]

        if element == target:
            return mid_ind

        if element > target:
            right_index = mid_ind - 1
        else:
            left_index = mid_ind + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
