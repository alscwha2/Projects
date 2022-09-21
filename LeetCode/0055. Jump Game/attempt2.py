"""
	Straightforward linear solution
"""
from typing import List


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		farthest = 0
		for i, num in enumerate(nums):
			if i > farthest:
				return False
			farthest = max(farthest, i + num)
		return True

# argv[1]
# print(Solution())
