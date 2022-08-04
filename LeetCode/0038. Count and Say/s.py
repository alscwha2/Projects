from typing import List
from sys import argv as argv

class Solution:
	def countAndSay(self, n: int) -> str:
		if n == 1:
			return "1"

		previous = self.countAndSay(n-1)
		count = 1
		digit = str(previous[0]) # because countAndSay will never return the empty string
		returnString = ''

		for i in range(1, len(previous)):
			if previous[i] == previous[i-1]:
				count += 1
			else:
				returnString += str(count) + digit
				count = 1
				digit = str(previous[i])

		return returnString + str(count) + digit

# argv[1]
# print(Solution())