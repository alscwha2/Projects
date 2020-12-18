from typing import List
from sys import argv as argv
from collections import deque

'''
	scan left to right
	keep track of what height coming next will give you how much more yield
	when you actually capture something put it in capacity
	return at end of iteration

'''

class Solution:
	def trap(self, height: List[int]) -> int:
		capacity = 0

		walls = deque([(0,-1)])
		lowest = 0
		for i,wall in enumerate(height):

			if wall == lowest:
				walls.pop()

			elif wall > lowest:
				previous = lowest
				try:
					while wall > previous:
						lowest = walls[-1]

						added = (min(lowest[0], wall) - previous) * (i-lowest[1]-1)
						capacity += added

						previous = lowest[0]
						if previous <= wall:
							walls.pop()
				except:
					pass

			lowest = wall
			walls.append((wall,i))
		return capacity
		

# argv[1]
print(Solution().trap([4,2,0,3,2,5]))