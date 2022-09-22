from typing import List


class Solution:
	def jump(self, nums: List[int]) -> int:
		jumps = 0
		i, end = 0, len(nums)-1

		# if you're not at the end yet
		while i < end:
			num = nums[i]

			# if you can make it in one jump, do it
			if i + num >= end:
				return jumps+1

			# else find the most strategic position to jump to
			maxrange, maxindex = 0,0
			for j in range(i+1, i+num+1):
				if j + nums[j] > maxrange:
					maxrange, maxindex = j+nums[j], j

			# jump to that position
			i = maxindex
			jumps += 1

		return jumps


# argv[1]
# print(Solution())
