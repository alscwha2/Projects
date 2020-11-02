from typing import List
from sys import argv

'''
	Trying to simulate long division here
'''
class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		# dealing with signs
		negative = False
		if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
			negative = True
		dividend = abs(dividend)
		divisor = abs(divisor)

		if dividend < divisor:
			return 0 

		dividend = [d for d in str(dividend)]
		shifts = len(dividend) - len(str(divisor))
		result = ''

		while shifts >= 0:
			# shift the previous result to the left, add a 0 in the ones place
			result = int(str(result) + '0')

			# get all of the digits before the next shift
			tail = len(dividend) - shifts
			localDividend = int(''.join(d for d in dividend[:tail]))
			while(localDividend >= divisor):
				result += 1
				localDividend -= divisor

			# append the remainder to the rest of the dividend
			dividend = [d for d in str(localDividend)] + dividend[tail:] if localDividend != 0 else dividend[tail:]

			shifts -= 1

		result = result if not negative else 0 - result
		return result if -pow(2,31) <= result <= pow(2,31)-1 else pow(2,31)-1

# sys.argv[1]
print(Solution().divide(2147483647,2))