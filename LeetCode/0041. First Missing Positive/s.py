from typing import List
from sys import argv as argv
from heapq import heappush, heappop

'''
	sort nums O(NlogN)
	skip all negatives and zero
	make sure next one is 1 else return 1
	make sure that each one increments by 1 else return last+1
	finally return last num in list +1

'''

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		if nums == []:
			return 1

		nums = sorted(nums)
		i = 0
		for i,num in enumerate(nums):
			if num > 0:
				break
		if nums[i] != 1:
			return 1
		last = 1
		for i in range(i+1, len(nums)):
			if nums[i] == last:
				continue
			if nums[i] != last+1:
				return last+1
			last = nums[i]
		return last+1


print(Solution().firstMissingPositive([1,2,3,4,5,6,7,8,9,20]))
