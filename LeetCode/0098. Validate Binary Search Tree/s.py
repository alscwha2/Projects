from typing import List
from sys import argv as argv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		last = [-inf]
		def inorder(node): 
			if not node:
				return True
			if not inorder(node.left):
				return False
			if node.val <= last[0]:
				return False
			last[0] = node.val
			return inorder(node.right)
		return inorder(root)







# argv[1]
# print(Solution())
