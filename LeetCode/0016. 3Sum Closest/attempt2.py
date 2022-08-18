"""
O(N ** 2) speed, space could be either O(1) or O(N) depending on sorted impl
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                closest = closest if abs(closest - target) < abs(current - target) else current
                if current > target:
                    k -= 1
                elif current < target:
                    j += 1
                else:
                    return current
        return closest


print(Solution().threeSumClosest([-1,2,1,-4], 1))