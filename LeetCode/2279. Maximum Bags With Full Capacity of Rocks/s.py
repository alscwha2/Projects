"""
    I'd like to make this code more elegant, and rename the variables
"""
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needed_to_fill = [*map(lambda limit, current: limit-current, capacity, rocks)]
        needed_to_fill.sort()
        full_bags = 0
        for needed in needed_to_fill:
            if additionalRocks - needed < 0:
                break
            else:
                full_bags += 1
                additionalRocks -= needed
        return full_bags
