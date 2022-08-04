from typing import List
from sys import argv as argv

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		if len(nums) <= 1:
			return [nums]
			
		answer = []
		for i,num in enumerate(nums):
			for rest in self.permute(nums[:i] + nums[i+1:]):
				answer.append([num]+rest)
		return answer


# argv[1]
# print(Solution())
