from typing import List
from sys import argv as argv
from collections import defaultdict, deque

'''
	Find all edges that are not part of a cycle

	IM NOT GOOD ENOUGH AT GRAPH PROBLEM YET

	THIS SEEMS LIKE A PRETTY SIMPLE PROBLEM I JUST NEED TO LEARN GRAPHS
'''
class Solution:
	def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
		if len(connections) == n-1:
			return connections

		connections = set(tuple(connection) for connection in connections)
		neighbors = defaultdict(list)
		for a,b in connections:
			neighbors[a].append(b)
			neighbors[b].append(a)

		seen = defaultdict{bool}
		stack = deque()
		def dfs(node, parent=None):
			seen[node] = True
			stack.append(node)
			for neighbor in neighbors[node]:
				if seen[neighbor]:
					if neighbor is not parent:
						i = -3
						while current is not neighor:

						connections.difference_update(stack)
				else:
					dfs(neighbor, node)
			stack.pop()

		dfs(0)
		return list(connections)



		

# argv[1]
print(Solution().criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))
