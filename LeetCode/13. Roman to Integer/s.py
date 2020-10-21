class Solution:
	def romanToInt(self, s: str) -> int:
		numerals = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000
		}
		first = 0
		second = 0
		value = 0
		for i in range(len(s)):
			if not first:
				first = s[i]
				continue
			second = s[i]

			if numerals[second] > numerals[first]:
				value += numerals[second] - numerals[first]
				first = second = 0
			else:
				value += numerals[first]
				first = second
				second = 0
		
		return value if not first else value + numerals[first]

from sys import argv
print(Solution().romanToInt(argv[1]))