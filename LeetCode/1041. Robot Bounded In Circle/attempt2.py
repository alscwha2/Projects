from typing import List
from sys import argv as argv
from math import sin, cos, pi

'''
	This is trying to use math. This is all correct but the reason that it doesn't work is because floating point numbers 
		are not precise enough and therefore I'm not getting exact numbers.
	This would all be solved if I could just use sin and cos using degrees!
'''

class Solution:
	def isRobotBounded(self, instructions: str) -> bool:
		# state
		x,y = 0,0
		angle = 1/2

		# parse and execute instructions
		for instruction in instructions:
			if instruction == 'G':
				x += cos(pi * angle)
				y += sin(pi * angle)
			elif instruction == 'L':
				angle = (angle + 1/2) % (2)
			elif instruction == 'R':
				angle = (angle - 1/2) % (2)

		# interpret ending state
		if (x,y) != (0,0) and angle == 1/2:
			return False
		else:
			return True


# argv[1]
print(Solution().isRobotBounded('GLRLLGLL'))
