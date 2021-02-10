from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	BFS
	(only difference between this and iterative DFS is popleft() instead of pop())
'''

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		G = defaultdict(list)
		for a,b in edges:
			G[a].append(b)
			G[b].append(a)

		seen = defaultdict(bool)

		num_components = 0
		queue = deque()
		for node in range(n):
			if not seen[node]:
				num_components += 1
				queue.append(node)
				while queue:
					node = queue.popleft()
					for neighbor in G[node]:
						if not seen[neighbor]:
							queue.append(neighbor)
					seen[node] = True

		return num_components




# argv[1]
print(Solution().countComponents(4, [[2,3],[1,2],[1,3]]))