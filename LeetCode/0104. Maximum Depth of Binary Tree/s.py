from typing import List
from sys import argv as argv

'''
	simplest recursive code
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
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# argv[1]
# print(Solution())
