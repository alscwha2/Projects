from typing import List
from sys import argv as argv

'''
	O(k(n-k)) (if k = n/2 then this is 1/4 n^2)
	keep tracck of 2 largest
'''

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		nums = sorted([(num:i) for i,num in enumerate(nums)])
		windows = [-inf for _ in range(len(nums))]



# argv[1]
# print(Solution())
