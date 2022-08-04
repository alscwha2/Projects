# from sys import argv
# from typing import List
class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		return self.kSum(nums, target, 4)

	def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
		groups = set()
		if k > 2:
			for i in range(len(nums) - (k - 1)):
				for group in self.kSum(nums[i + 1:], target - nums[i], k-1):
					group.insert(0,nums[i])
					groups.add(tuple(group))
		else:
			return self.twoSum(nums, target)

		return [list(g) for g in groups]

	def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
		i = 0
		j = len(nums) - 1

		groups = set()
		while i < j:
			distance = target - nums[i] - nums[j]
			if distance is 0:
				groups.add((nums[i], nums[j]))
				i += 1
				j -= 1
				continue
			if distance > 0:
				i += 1
			else:
				j -= 1

		return [list(g) for g in groups]


# print(Solution().fourSum([int(s) for s in argv[1].split(',')], int(argv[2])))