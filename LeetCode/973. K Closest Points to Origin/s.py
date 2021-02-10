from typing import List
from sys import argv as argv
from math import sqrt

'''
	this is the doc's solution. Very cool.
'''

class Solution:
	def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
		points.sort(lambda p: p[0]**2 + p[1]**2)
		return points[:K]

# argv[1]
print(Solution().kClosest([[1,3],[-2,2]], 1))