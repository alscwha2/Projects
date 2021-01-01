from typing import List
from sys import argv as argv

'''
	binary search start interval immediately <= start
	binary serach start interval immediately >= end
'''

class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		start,end = newInterval
		i,j = 0,len(intervals)
		while i <= j:
			k = i + (j-i)//2
			if intervals[k][0] <= start:
				i = k+1
			else:
				j = k-1
		pred = j
		# j is going to be the interval whose start is immediately less than or equal to start
		
		i,j = 0,len(intervals)
		while i <= j:
			k = i + (j-i)//2
			if intervals[k][1] >= end:
				j = k-1
			else:
				i = k+1
		succ = i

		'''
		-1,0
		-1,n
		n-1,n
		-1,x
		x,n
		x,x
		'''





# argv[1]
# print(Solution())
