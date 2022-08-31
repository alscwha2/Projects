"""
    This version should be more efficient. We don't have to check whether the
        end is pointing at val unless the beginning is pointing at val
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] == val:
                while nums[end] == val:
                    end -= 1
                    if end < start:
                        return start
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            start += 1
        return start
