# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.

class Solution(object):
    def sortColors(self, nums):

        n = len(nums)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


solve = Solution()
print(solve.sortColors([2,0,2,1,1,0]))