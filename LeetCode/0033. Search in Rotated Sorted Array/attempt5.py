from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r if nums[r] == target else -1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            l_num, m_num, r_num = nums[l], nums[m], nums[r]
            if l_num < r_num:
                return binary_search(l, r)
            else:
                if m_num > target:
                    if m_num < l_num:
                        r = m - 1
                    else:
                        if l_num > target:
                            l = m + 1
                        else:
                            r = m - 1
                elif m_num < target:
                    if m_num > l_num:
                        l = m + 1
                    else:
                        if r_num < target:
                            r = m - 1
                        else:
                            l = m + 1
                else:
                    return m

        return -1
