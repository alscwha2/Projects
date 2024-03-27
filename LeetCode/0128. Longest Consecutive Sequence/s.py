from typing import List

'''
	DO A UNION-FIND
'''

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		group = {num:num for num in nums}
		size = {num:1 for num in nums}

		def find(a):
			root = a
			while group[root] != root:
				root = group[root]
			while a != root:
				parent = group[a]
				group[a] = root
				a = parent
			return root

		def union(a,b):
			try:
				a_root, b_root = find(a), find(b)
				if a_root != b_root:
					group[a_root] = b_root
					size[b_root] += size[a_root]
			except KeyError:
				pass

		for num in nums:
			union(num, num-1)
			union(num, num+1)

		return max(size.values(), default=0)

