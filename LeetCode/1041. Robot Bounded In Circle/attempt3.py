from typing import List
from sys import argv as argv

class Solution:
	def isRobotBounded(self, instructions: str) -> bool:
		# state
		x,y = 0,0
		angle = 90
		xdisplacement = {0:1, 90:0, 180:-1, 270:0}
		ydisplacement = {0:0, 90:1, 180:0, 270:-1}
		# parse and execute instructions
		for instruction in instructions:
			if instruction == 'G':
				x += xdisplacement[angle]
				y += ydisplacement[angle]
			elif instruction == 'L':
				angle = (angle + 90) % 360
			elif instruction == 'R':
				angle = (angle - 90) % 360

		# interpret ending state
		if (x,y) != (0,0) and angle == 90:
			return False
		else:
			return True


# argv[1]
# print(Solution())
