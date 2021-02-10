from typing import List
from sys import argv as argv

'''
	iterate though list backwards, 
		changing all of the entries to entry.split(' ')
		moving all of the digit logs to the back
			O(N) time O(1) space
	sort the letter log portion of the list according to the sort rules
		O(NlogN) time
		O(N) space
'''

class Solution:
	def reorderLogFiles(self, logs: List[str]) -> List[str]:
		nextDigitSlot = len(logs)-1
		for i in range(len(logs)-1, -1, -1):
			log = logs[i]
			if log[log.index(' ')+1].isnumeric():
				logs[nextDigitSlot], logs[i] = logs[i], logs[nextDigitSlot]
				nextDigitSlot -= 1
		
		for i in range(nextDigitSlot+1):
			part = logs[i].partition(' ')
			logs[i] = (part[2], part[0])

		logs[:nextDigitSlot+1] = sorted(logs[:nextDigitSlot+1])

		for i in range(nextDigitSlot+1):
			logs[i] = ' '.join(reversed(logs[i]))
		return logs
		

# argv[1]
# print(Solution())
