from typing import List
from sys import argv as argv
import profile

'''
	The 'backtracking' method defined in the solution doc on leetcode.
	This is better in every way...
	Although the dp method might be better for much larger arrays
'''

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

		def finishGroup(group, target, index):
			completed = []
			for i in range(index, len(candidates)):
				num = candidates[i]
				if num < target:
					completed.extend(finishGroup(group + [num], target - num, i))
				elif num > target:
					return completed
				else:
					return completed + [group + [num]]
			return completed


		candidates = sorted(candidates)
		return finishGroup([], target, 0)



		
profile.run('Solution().combinationSum([i for i in range(1, 20)],40)')