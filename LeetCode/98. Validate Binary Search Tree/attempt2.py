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
		def isValidMinMax(node, min=-inf, max=inf):
			if not node:
				return True
			if node.val <= min or node.val >= max:
				return False
			return isValidMinMax(node.left, min, node.val) and isValidMinMax(node.right, node.val, max)
		return isValidMinMax(root)





# argv[1]
# print(Solution())
