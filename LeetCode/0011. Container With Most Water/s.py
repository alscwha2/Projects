"""
Linear time, constant space
"""

from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		# calculate end-to-end volume
		l, r = 0, len(height) - 1
		best = 0

		while r > l:
			if height[r] > height[l]:
				current = height[l] * (r-l)
				l += 1
			else:
				current = height[r] * (r-l)
				r -= 1
			best = max(best, current)

		return best


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))