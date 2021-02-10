from typing import List
from sys import argv as argv
from collections import defaultdict, deque


'''
	BFS

	create new Node with empty neighbors
		save new node in map
	for each neighbor:
		create new node for neighbor
			save new node in map
		add to neighbor list
		repeat for newly created node
'''

"""
# Definition for a Node.
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		if not node:
			return None

		nodes = {1 : Node(1)}
		not_processed = deque([node])
		while not_processed:
			node = not_processed.popleft()
			new_node = nodes[node.val]
			for neighbor in node.neighbors:
				if not neighbor.val in nodes:
					nodes[neighbor.val] = Node(neighbor.val)
					not_processed.append(neighbor)
				new_node.neighbors.append(nodes[neighbor.val])

		return nodes[1]

# argv[1]
# print(Solution())