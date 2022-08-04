from typing import List
from sys import argv as argv

'''
	The obvious way to get rid of duplicates is to just take 
		all of the permutations, turn them into tuples, but them
		in a set

	but that's not what we did here

	We avoided computing duplicates by making sure that we only considered each unique value
		to be in the beginning of the array ONE time
	This was accomplished by sorting the array and skipping any number which was the same as previous

'''

class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		nums = sorted(nums)

		def permute(nums):
			if len(nums) <= 1:
				return [nums]

			answer = [[nums[0]] + rest for rest in permute(nums[1:])]
			for i in range(1, len(nums)):
				if nums[i] == nums[i-1]:
					continue
				answer.extend([[nums[i]] + rest for rest in permute(nums[:i] + nums[i+1:])])
			return answer

		return permute(nums)





# argv[1]
# print(Solution())
