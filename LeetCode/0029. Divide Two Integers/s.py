from typing import List
from sys import argv

'''
	This solution is way too slow. Try to run it and see what happens
'''
class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		if dividend == 0:
			return 0

		result = 0
		negative = False

		if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
			negative = True
		if dividend < 0:
			dividend = 0 - dividend
		if divisor < 0:
			divisor = 0 - divisor
		while dividend >= divisor:
			print(locals())
			dividend -= divisor
			result += 1

		if result > pow(2, 31)-1:
			return pow(2,31)-1

		return result if not negative else 0 - result

# sys.argv[1]
print(Solution().divide(-pow(2, 31), -1))
