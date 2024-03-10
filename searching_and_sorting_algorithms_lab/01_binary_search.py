def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        element_mid = nums[mid]

        if element_mid == target:
            return mid

        if element_mid > target:
            right = mid - 1

        if element_mid < target:
            left = mid + 1

    return -1


nums = [int(ch) for ch in input().split(' ')]
target = int(input())
print(binary_search(nums, target))