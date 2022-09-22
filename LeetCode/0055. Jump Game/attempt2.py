"""
	Straightforward linear solution
"""
from typing import List


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		farthest = 0
		for position, jump_length in enumerate(nums):
			if position > farthest:
				return False
			farthest = max(farthest, position + jump_length)
		return True

# argv[1]
# print(Solution())
