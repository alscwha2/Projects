from typing import List
from sys import argv as argv

'''
	sliding window
	time O(N)
	space O(1)
'''
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		if not nums:
			return 0

		sum = nums[0]
		count = 1 if sum == k else 0

		if len(nums) == 1:
			return count

		i = 0
		for j in range(1, len(nums)):
			sum += nums[j]
			while sum > k:
				sum -= nums[i]
				i += 1
			if sum == k:
				count += 1
		return count






# argv[1]
print(Solution().subarraySum([-1,-1,1],0))