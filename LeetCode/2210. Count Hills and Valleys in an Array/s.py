from itertools import pairwise
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        total_hills_and_valleys = 0
        UP, DOWN, STEADY = 0, 1, 2
        previous_direction = STEADY
        for a, b in pairwise(nums):
            current_direction = STEADY
            if b > a:
                current_direction = UP
            elif b < a:
                current_direction = DOWN
            else:
                continue
            if (current_direction == UP and previous_direction == DOWN) or (current_direction == DOWN and previous_direction == UP):
                total_hills_and_valleys += 1
            previous_direction = current_direction
        return total_hills_and_valleys
