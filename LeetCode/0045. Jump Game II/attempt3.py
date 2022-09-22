from typing import List


class Solution:
	def jump(self, nums: List[int]) -> int:
		jumps = 0
		previous_jump_range = 0
		next_jump_range = 0
		for current_position, jump_length in enumerate(nums):
			next_jump_range = max(next_jump_range, current_position + jump_length)
			if current_position == previous_jump_range != len(nums) - 1:
				jumps += 1
				previous_jump_range = next_jump_range
		return jumps



print(Solution().jump([2,3,1,1,4]))
