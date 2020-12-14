from typing import List
from sys import argv as argv
from heapq import merge as merge
import profile

'''
	this was the best that I could do
'''

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates = set(candidates)

		dp = dict()
		
		def cs(target: int) -> List[List[int]]:
			sets = set()
			if target in candidates:
				sets.add(tuple([target]))

			i = 1
			j = target - 1
			while i <= j:
				ipairs = dp[i] if i in dp else cs(i)
				jpairs = dp[j] if j in dp else cs(j)
				if ipairs and jpairs:
					for ipair in ipairs:
						for jpair in jpairs:
							pair = tuple(merge(ipair, jpair))
							sets.add(pair)
				i += 1
				j -= 1
			dp[target] = [list(group) for group in sets]
			return dp[target]

		return cs(target)
		
profile.run('print(Solution().combinationSum([i for i in range(1,20)],20))')