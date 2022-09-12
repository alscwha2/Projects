from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(l, r, comparator):
            while l <= r:
                m = (l + r) // 2
                if comparator(target, nums[m]):
                    r = m - 1
                else:
                    l = m + 1
            return l, r

        _, r = binary_search(0, len(nums) - 1, lambda a, b: a < b)

        if r == -1 or nums[r] != target:
            return [-1, -1]

        l, _ = binary_search(0, r, lambda a,b: a <= b)
        return [l, r]

print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
