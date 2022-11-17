from typing import List
from collections import defaultdict

'''
	recursive DFS
'''

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		G = defaultdict(list)
		for a,b in edges:
			G[a].append(b)
			G[b].append(a)

		seen = defaultdict(bool)

		def dfs(node):
			seen[node] = True
			for neighbor in G[node]:
				if not seen[neighbor]:
					dfs(neighbor)

		num_components = 0
		for node in range(n):
			if not seen[node]:
				num_components += 1
				dfs(node)

		return num_components


# argv[1]
print(Solution().countComponents(4, [[2,3],[1,2],[1,3]]))