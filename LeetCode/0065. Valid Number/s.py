from typing import List
from sys import argv as argv
'''
	int = neg|pos|neut
	neg = -neut
	pos = +neut
	float = int.neut
	exp = float|int e int



	This question is useful for practicing writing grammars
	but for this to work you need a complete list of what is valid for each type
		which made this frustraing to solve because I just kept on submitting
		it and got errors for these edge cases and a lot of them you have no 
		intuition as to whether it should be valid or not.

'''

class Solution:
	def isNumber(self, s: str) -> bool:
		def isNeut(s):
			return s.isnumeric() or not s

		def isInt(s):
			if not s:
				return True
			if s[0] == '-' or s[0] == '+':
				s = s[1:]
				if not s:
					return False
			return isNeut(s)

		def isFloat(s):
			if '.' not in s:
				return False
			if s[0] == '-' or s[0] == '+':
				s = s[1:]
			tokens = s.split('.')
			if len(tokens) != 2:
				return False
			integer,decimal = tokens
			if not integer and not decimal:
				return False
			return isNeut(integer) and isNeut(decimal)


		def isExp(s):
			if not 'e' in s:
				return False
			tokens = s.split('e')
			if len(tokens) != 2:
				return False
			base,power = tokens
			if not base or not power:
				return False
			return (isFloat(base) or isInt(base)) and isInt(power)

		s = s.strip()
		if not s:
			return False
		if 'e' in s:
			return isExp(s)
		if '.' in s:
			return isFloat(s)
		return isInt(s)


# argv[1]
# print(Solution())
