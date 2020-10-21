class Solution:
	def intToRoman(self, num: int) -> str:
		def digitToRoman(powerTen: int, digit: int) -> str:
			ones = {0: 'I', 1: 'X', 2: 'C', 3: 'M'}
			fives = {0: 'V', 1: 'L', 2: 'D'}

			if digit == 9:
				return ones[powerTen] + ones[powerTen + 1]
			if digit == 4:
				return ones[powerTen] + fives[powerTen]

			romanDigit = fives[powerTen] if (digit // 5) else ''
			for i in range(digit % 5):
				romanDigit += ones[powerTen]

			return romanDigit
	
		romanString = ''

		# Loop through digits using % and //
		# Keep track of order of ten using powerTen as index
		# Can only ever have at most 4 digits (because of problem definition)
		for powerTen in range(4):
			if num == 0:
				break
			digit = num % 10
			num = num // 10
			# putting this in the end for tail-recursion, would have put after digit line
			romanString = digitToRoman(powerTen, digit) + romanString

		return romanString

