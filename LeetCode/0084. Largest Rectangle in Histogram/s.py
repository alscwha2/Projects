from typing import List
from sys import argv as argv
from collections import deque

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		largest = 0
		stack = deque([(0,0)])

		def getLastHeight():
			return stack[-1][1]

		for i,height in enumerate(heights):
			if height > getLastHeight():
				stack.append((i,height))
			elif height < getLastHeight():
				lastIndex = -1
				while height < getLastHeight():
					lastIndex, lastHeight = stack.pop()
					capacity = lastHeight*(i-lastIndex)
					largest = max(largest, capacity)
				if not height == getLastHeight():
					stack.append((lastIndex, height))
					
		n = len(heights)
		for i,height in stack:
			capacity = height * (n-i)
			largest = max(largest, capacity)
		return largest			


# argv[1]
# print(Solution())
