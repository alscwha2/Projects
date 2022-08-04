from typing import List
from sys import argv as argv

class Solution:
	def mirrorReflection(self, p: int, q: int) -> int:
		def gcd(a,b):
			if a == b:
				return a
			if a < b:
				return gcd(a, b-a)
			else:
				return gcd(a-b, b)

		SOUTH, SOUTH, WEST, EAST= 0, 1, 0, 1
		CORNER = [[None, 0], [2, 1]]

		greatest_divisor = gcd(p, q)
		num_horizontal_bounces = p // greatest_divisor
		latitude = num_horizontal_bounces % 2
		longitude = (num_horizontal_bounces * q) // (2 * p)


		return CORNER[longitude][latitude]


		

# argv[1]
print(Solution().mirrorReflection(24,36))