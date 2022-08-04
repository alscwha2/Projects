from typing import List
from sys import argv as argv

'''
	Recursive approach
'''

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		def backtrack(n):
			if n == -1:
				return [[]]

			answer = []
			rest = backtrack(n-1)
			for comb in rest:
				answer.append(comb)
				answer.append(comb + [nums[n]])
			return answer

		return backtrack(len(nums)-1)

# argv[1]
print(Solution().subsets([i for i in range(3)]))
