# You are given a 0-indexed array nums of length n containing distinct positive integers.
# Return the minimum number of right shifts required to sort nums and -1 if this is not possible.
#
# A right shift is defined as shifting the element at index i to index (i + 1) % n, for all indices.


class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sorted_list = sorted(ch for ch in nums)
        if nums == sorted_list:
            return 0

        counter = 0
        for _ in range(n):
            counter += 1
            last_element = nums.pop()
            nums.insert(0, last_element)

            if nums == sorted_list:
                return counter

        return -1


solve = Solution()
print(solve.minimumRightShifts([3,4,5,1,2]))
print(solve.minimumRightShifts([1, 3, 5]))
print(solve.minimumRightShifts([2, 1, 4]))