from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	Iterative DFS
'''

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		G = defaultdict(list)
		for a,b in edges:
			G[a].append(b)
			G[b].append(a)

		seen = defaultdict(bool)

		num_components = 0
		stack = deque()
		for node in range(n):
			if not seen[node]:
				num_components += 1
				stack.append(node)
				while stack:
					node = stack.pop()
					for neighbor in G[node]:
						if not seen[neighbor]:
							stack.append(neighbor)
					seen[node] = True

		return num_components




# argv[1]
print(Solution().countComponents(4, [[2,3],[1,2],[1,3]]))