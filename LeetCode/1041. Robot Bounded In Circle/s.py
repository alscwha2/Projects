from typing import List
from sys import argv as argv

class Solution:
	def isRobotBounded(self, instructions: str) -> bool:
		# state
		x,y = 0,0
		angle = 90

		# parse and execute instructions
		for instruction in instructions:
			if instruction == 'G':
				if angle == 90:
					y += 1
				elif angle == 180:
					x -= 1
				elif angle == 270:
					y -= 1
				else:
					x += 1
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
