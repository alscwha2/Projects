from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            else:
                lnum, mnum, rnum = nums[l], nums[m], nums[r]
                if mnum > target:
                    if mnum < lnum:
                        r = m - 1
                    else:
                        if lnum > target:
                            l = m + 1
                        else:
                            r = m - 1
                elif mnum < target:
                    if mnum > lnum:
                        l = m + 1
                    else:
                        if rnum < target:
                            r = m - 1
                        else:
                            l = m + 1
                else:
                    return m

        return -1
