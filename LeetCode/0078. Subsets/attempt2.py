from typing import List
from sys import argv as argv
from collections import deque

'''
	Iterative approach
'''

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		done, new = [[]], deque()

		for num in nums:
			for subset in done:
				new.append(subset + [num])
			done.extend(new)
			new.clear()
		return done

# argv[1]
print(Solution().subsets([i for i in range(3)]))
