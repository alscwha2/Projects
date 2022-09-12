from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_first_element():
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] < nums[r]:
                    return l
                else:
                    m = (l + r) // 2
                    if nums[l] <= nums[m]:
                        l = m + 1
                    else:
                        r = m
            return r

        def get_pivoted_index(n):
            return (first_element_index + n) % len(nums)

        first_element_index = find_first_element()
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            current = nums[get_pivoted_index(m)]
            if current < target:
                l = m + 1
            elif current > target:
                r = m - 1
            else:
                return get_pivoted_index(m)
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
