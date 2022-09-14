from typing import List

"""
    I think that this is the cleanest code yet. Procedural
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def in_bounds(num):
            return 1 <= num <= len(nums)

        def put_nums_in_order():
            for i in range(len(nums)):
                while in_bounds(num := nums[i]) and num != nums[num - 1]:
                    swap(i, num - 1)

        put_nums_in_order()

        for expected, actual in enumerate(nums, 1):
            if expected != actual:
                return expected
        return len(nums) + 1


print(Solution().firstMissingPositive([3,4,-1,1]))