# from sys import argv
# from typing import List
class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		quads = set()
		i = 0

		while i < len(nums) - 3:
			j = i + 1
			while j < len(nums) - 2:
				rest = target - nums[i] - nums[j]
				k = j + 1
				l = len(nums) - 1

				while l > k:
					distance = rest - nums[k] - nums[l]
					if distance is 0:
						quads.add((nums[i], nums[j], nums[k], nums[l]))
						k += 1
						l -= 1
						continue
					if distance < 0:
						l -= 1
					else:
						k += 1
				j += 1
				# while j < len(nums) - 2 and nums[j] is nums[j - 1]:
				# 	j += 1
			i += 1
			# while i < len(nums) and nums[i] is nums[i - 1]:
			# 	i += 1
		return [list(q) for q in quads]

# print(Solution().fourSum([int(s) for s in argv[1].split(',')], int(argv[2])))