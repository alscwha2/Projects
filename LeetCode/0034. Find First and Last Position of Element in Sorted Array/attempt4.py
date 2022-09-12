from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if r == -1 or nums[r] != target:
            return [-1, -1]

        l, j = 0, r
        while l <= j:
            m = (l + j) // 2
            if target <= nums[m]:
                j = m - 1
            else:
                l = m + 1

        return [l, r]
