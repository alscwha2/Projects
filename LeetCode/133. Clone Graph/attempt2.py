from typing import List
from sys import argv as argv
from collections import defaultdict, deque


'''
	DFS
'''

"""
# Definition for a Node.
class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	nodes = {}
	def cloneGraph(self, node: 'Node') -> 'Node':
		if not node:
			return None

		if node in self.nodes:
			return self.nodes[node]

		new_node = Node(node.val)
		self.nodes[node] = new_node

		for neighbor in node.neighbors:
			new_node.neighbors.append(self.cloneGraph(neighbor))
		return self.nodes[node]


# argv[1]
print('hello world')