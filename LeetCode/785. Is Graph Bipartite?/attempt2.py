from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	Using DFS
	Make sure that there are no odd-numbered cycles
'''

class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		n = len(graph)
		seen = [False for _ in range(n)]
		index = {}
		self.current = 0

		def dfs(node):
			seen[node] = True
			index[node] = self.current
			self.current += 1
			for neighbor in graph[node]:
				if seen[neighbor]:
					if neighbor in index:
						if (self.current - index[neighbor]) % 2:
							return False
				else:
					if not dfs(neighbor):
						return False
			del index[node]
			self.current -= 1
			return True

		answer = True
		for node in range(n):
			if answer and not seen[node]:
				answer = dfs(node)
		return answer




# argv[1]
print(Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))