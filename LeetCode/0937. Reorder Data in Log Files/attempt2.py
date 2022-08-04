from typing import List
from sys import argv as argv

'''
	From the solution doc. This is basically what I wanted to do.

		class Solution:
			def reorderLogFiles(self, logs: List[str]) -> List[str]:
				def cmp(log):
					id,rest = log.split(' ', maxsplit=1)
					return (0,rest,id) if rest[0].isalpha() else (1,)
				logs.sort(key=cmp)
				return logs

	- I didn't know that the sort function would preserve order
	- I didn't know that the sort function would be just as eficient as sorting the digits the way that I did
		- is it really?
	- I didn't know that the comparator was not recomputed every time
'''

class Solution:
	def reorderLogFiles(self, logs: List[str]) -> List[str]:
		nextDigitSlot = len(logs)-1
		for i in range(len(logs)-1, -1, -1):
			log = logs[i]
			if log[log.index(' ')+1].isnumeric():
				logs[nextDigitSlot], logs[i] = logs[i], logs[nextDigitSlot]
				nextDigitSlot -= 1

		logs[:nextDigitSlot+1] = sorted(logs[:nextDigitSlot+1], key = lambda log:tuple(reversed(log.split(' ',maxsplit=1))))
		return logs
		

# argv[1]
# print(Solution())
