"""
    O(NlogN)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        in_order = [(tallness, index) for index, tallness in enumerate(height)]
        in_order.sort(reverse=True)
        i = j = in_order[0][1]
        for tallness, index in in_order:
            i = min(i, index)
            j = max(j, index)
            max_water = max(max_water, (j-i) * tallness)
        return max_water

