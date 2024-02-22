# AVG Time Complexity O(n)

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None


print(linear_search([1, 6, 2, 4], 2))
