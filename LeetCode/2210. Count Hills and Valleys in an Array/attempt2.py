from itertools import pairwise
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        total_hills_and_valleys = 0
        UP, DOWN, STEADY = 0, 1, 2
        previous_direction = STEADY
        for a, b in pairwise(nums):
            if b > a:
                if previous_direction == DOWN:
                    total_hills_and_valleys += 1
                previous_direction = UP
            elif b < a:
                if previous_direction == UP:
                    total_hills_and_valleys += 1
                previous_direction = DOWN
        return total_hills_and_valleys
