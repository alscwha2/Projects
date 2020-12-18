from typing import List
from sys import argv as argv

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		if not intervals:
			return intervals

		intervals = [tuple(interval) for interval in intervals]
		intervals = sorted(intervals)

		combined = []

		current = list(intervals[0])
		for interval in intervals:
			if interval[0] <= current[1]:
				current = [current[0], max(current[1], interval[1])]
			else:
				combined.append(current)
				current = list(interval)
		combined.append(current)
		
		return combined


# argv[1]
# print(Solution())
