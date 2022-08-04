from typing import List
from sys import argv as argv

'''
	Let's just call this whole thing a failure.
'''

class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		i,j = 0,len(nums)
		while i <= j:
			k = i + (j-i)//2
			if nums[i] == target or nums[k] == target:
				return True
			if target > nums[i]:
				if target < nums[k]:
					j = k-1
					i = i+1
				elif target > nums[k]:
					i = k+1
			elif target < nums[i]:
				if target < nums[k]:
					i = k+1
				elif target > nums[k]:
					i = k+1
		return False



# argv[1]
print(Solution().search([1,3,1,1,1],3))