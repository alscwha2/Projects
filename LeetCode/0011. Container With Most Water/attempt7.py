"""
    O(N)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            left_wall = height[i]
            right_wall = height[j]
            horizontal_length = j-i
            max_water = max(max_water, horizontal_length * min(left_wall, right_wall))

            if left_wall <= right_wall:
                i += 1
            if right_wall <= left_wall:
                j -= 1
        return max_water
