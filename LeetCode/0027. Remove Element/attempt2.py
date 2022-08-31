"""
    This is an optimization over the previous solution, since this only
        writes values when absolutely necessary
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
            else:
                if nums[start] == val:
                    nums[start], nums[end] = nums[end], nums[start]
                    end -= 1
                start += 1
        return start
