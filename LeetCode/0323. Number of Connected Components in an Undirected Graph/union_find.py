from typing import List
from collections import defaultdict

'''
	Union Find
'''

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		class keydefaultdict(defaultdict):
			def __missing__(self, key):
				return key

		parent = keydefaultdict()
		num_components = n

		def Union(a,b):
			a_component, b_component = Find(a), Find(b)
			if a_component != b_component:
				parent[b_component] = a_component
				nonlocal num_components
				num_components -= 1

		def Find(node):
			if parent[node] != node:
				parent[node] = Find(parent[node])
			return parent[node]

		for edge in edges:
			Union(*edge)
		return num_components

# argv[1]
print(Solution().countComponents(4, [[2,3],[1,2],[1,3]]))