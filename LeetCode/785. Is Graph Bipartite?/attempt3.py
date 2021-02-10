from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	Using DFS and coloring
'''

class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		def other(group):
			return 1 if not group else 0
		n = len(graph)
		seen = [False for _ in range(n)]
		group = [0 for _ in range(n)]

		for node in range(n):
			if seen[node]:
				continue
			seen[node] = True
			stack = deque([node])
			while stack:
				node = stack.pop()
				node_group = group[node]
				for neighbor in graph[node]:
					if seen[neighbor]:
						if group[neighbor] == node_group:
							return False
					else:
						group[neighbor] = other(node_group)
						stack.append(neighbor)
						seen[neighbor] = True

		return True




# argv[1]
print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))