from typing import List
from sys import argv as argv
from collections import deque

'''
	Trying to do this DFS style with a stack instead of recursion
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0
		depth = 0
		queue = deque([root])
		next = deque()
		while queue:
			depth += 1
			for node in queue:
				if node.left:
					next.append(node.left)
				if node.right:
					next.append(node.right)
			queue,next = next,queue
			next.clear()
		return depth


# argv[1]
# print(Solution())
