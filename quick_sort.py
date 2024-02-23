def quick_sort(nums, start, end):
    # BASE CASE
    if start >= end:
        return

    #Pre-action
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]

    # Recursive call
    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)

    # Post-Action
    return nums

nums = [64, 34, 25, 5, 22, 11, 90, 12]
nums = quick_sort(nums, 0, len(nums) - 1)
print(nums)