from typing import List
from sys import argv as argv
'''
	don't have to deal with sorting.
	create an ordered hashset (using a dict here becaue it's ordered) of numbers 1 through n+1
	remove all of the ones that we have already
	return the smallest one that we don't have (its in order so we know)

'''
class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		needed = {i:0 for i in range(1, len(nums) + 2)}
		for num in nums:
			try:
				del needed[num]
			except:
				pass
		return list(needed)[0] if needed != {} else 1


print(Solution().firstMissingPositive([1,2,0]))