from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	Using BFS and two queues
	Make sure than any back edges point to nodes in the opposite group
'''

class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		n = len(graph)
		seen = [False for _ in range(n)]
		group = [0 for _ in range(n)]

		for node in range(n):
			if seen[node]:
				continue
			first_level = None
			second_level = deque([node])
			current_group, other_group = 1, 2

			while second_level:
				first_level = second_level
				second_level = deque()

				for node in first_level:
					for neighbor in graph[node]:
						if seen[neighbor]:
							if group[neighbor] == current_group:
								return False
						else:
							second_level.append(neighbor)
							group[neighbor] = other_group
							seen[neighbor] = True
				current_group, other_group = other_group, current_group
		return True




# argv[1]
print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))