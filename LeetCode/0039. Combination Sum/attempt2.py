from typing import List

'''
	The 'backtracking' method defined in the solution doc on leetcode.
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
