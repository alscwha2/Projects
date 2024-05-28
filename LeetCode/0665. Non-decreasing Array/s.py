from typing import List
from itertools import pairwise


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def can_be_solved_by_switching_one_number(b):
            a = b-1

            if b == 1 or b == len(nums) - 1:
                return True
            if nums[a-1] <= nums[b] or nums[a] <= nums[b+1]:
                return True
            return False

        already_have_one_decrease = False
        for b in range(1, len(nums)):
            a = b-1
            if nums[b] < nums[a]:
                if already_have_one_decrease:
                    return False
                already_have_one_decrease = True

                if not can_be_solved_by_switching_one_number(b):
                    return False
        return True
