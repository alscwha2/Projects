from typing import List
from sys import argv as argv

class Solution:
	def mirrorReflection(self, p: int, q: int) -> int:

		def greatest_common_divisor(a, b):
			if a == b:
				return a
			if a < b:
				return greatest_common_divisor(a, b-a)
			else:
				return greatest_common_divisor(a-b, b)


		SOUTH, NORTH, WEST, EAST= 0, 1, 0, 1
		CORNER = [[None, 0], [2, 1]]

		greatest_divisor = greatest_common_divisor(p, q)
		num_horizontal_bounces = p // greatest_divisor
		latitude = num_horizontal_bounces % 2
		longitude = ((num_horizontal_bounces * q) // p) % 2


		return CORNER[longitude][latitude]


		

# argv[1]
print(Solution().mirrorReflection(24,36))