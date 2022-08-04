from typing import List
from sys import argv as argv

'''
	This could be cleaner
'''

class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:
		length = len(s)
		def divideintogroups(i, n):
			left = length-i
			if not n <= left <= 3*n:
				return []

			answer = []
			if n > 1:
				for group in divideintogroups(i+1, n-1):
					answer.append(s[i] + '.' + group)

				if left >= 2:
					if s[i] == '0':
						return answer
					for group in divideintogroups(i+2, n-1):
						answer.append(s[i:i+2] + '.' + group)

				if left >= 3 and int(s[i:i+3]) <= 255:
					for group in divideintogroups(i+3, n-1):
						answer.append(s[i:i+3] + '.' + group)

				return answer

			else:
				if left > 1 and (s[i] == '0' or int(s[i:]) > 255):
					return []
				else:
					return[s[i:]]

		return divideintogroups(0, 4)

# argv[1]
print(Solution().restoreIpAddresses("0000"))