"""
What changed here from attempt2 was that I was trying to find a way to prevent duplicates without 
	throwing everything into a set and then back into a list.
This ended up being a lot slower. I guess throwing everything into a set was the right way to go.

Regarding duplicates:
	In a sorted array all duplicates are next to each other
	if i and j are duplicates then you skip the next i iteration

	once j == j-1 or k == k+1 if j and k are duplicates then you must have already registered the duplicate in the previous iteration
	so it's safe to skip all j j and k k duplicates in the j k iteration

"""

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()

		sums = []
		for i in range(len(nums)):
			num = nums[i]
			if i is not 0 and num == nums[i-1]:
				continue

			complement = -num
			j = i + 1
			k = len(nums) - 1
			while j < k:
				sum = nums[j] + nums[k]
				if sum == complement:
					sums.append([num, nums[j], nums[k]])
				if sum <= complement:
					j += 1
					while j < k and nums[j] == nums[j-1]:
						j += 1
				if sum >= complement:
					k -= 1
					while j < k and nums[k] == nums[k+1]:
						k -= 1

		return sums