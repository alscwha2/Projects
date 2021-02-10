from typing import List
from sys import argv as argv

'''
	DO A UNION-FIND
'''

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0

		self.largest = 1
		group = {num:num for num in nums}
		size = {num:1 for num in nums}

		def union(a,b):
			try:
				a_root, b_root = find(a), find(b)
				if a_root != b_root:
					group[a_root] = b_root
					size[b_root] += size[a_root]
					self.largest = max(self.largest, size[b_root])
			except KeyError as err:
				pass

		def find(a):
			root = a
			while group[root] != root:
				root = group[root]
			while a != root:
				parent = group[a]
				group[a] = root
				a = parent
			return root

		for num in nums:
			union(num, num-1)
			union(num, num+1)

		answer, self.largest = self.largest, 0
		return answer

# argv[1]
# print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))