from typing import List
from sys import argv as argv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		def traverse(node, log=[]):
			if not node:
				return log
			traverse(node.left, log)
			log.append(node.val)
			return traverse(node.right, log)

		return traverse(root)
		

# argv[1]
# print(Solution())
