from sys import argv

class Solution:
	def myAtoi(self, s: str) -> int:
		#whitespace
		s = s.strip(" ")
		#+ - int
		sign = -1 if s[0] == '-' else 1
		s = s[1:] if s[0] == '-' or s[0] == '+' else s

		returnint = 0
		#loop til stop
		for i in range(len(s)):
			if s[i].isnumeric():
				returnint *= 10
				returnint += int(s[i])
			else:
				break
				
		return returnint * sign



print(Solution().myAtoi(argv[1]))