from typing import List
from sys import argv as argv

'''
	the answer they probably wanted
'''

class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		last = [1]
		for i in range(rowIndex):
			next = [1]
			for j in range(1,len(last)):
				next.append(last[j-1] + last[j])
			next.append(1)
			last = next
		return last


# argv[1]
# print(Solution())
