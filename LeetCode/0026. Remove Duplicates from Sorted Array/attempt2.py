from typing import List
from sys import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		newarray = list(set(nums))
		newarray.sort()
		for i in range(len(newarray)):
			nums[i] = newarray[i]
		return len(newarray)

sys.argv[1]
print(Solution())
