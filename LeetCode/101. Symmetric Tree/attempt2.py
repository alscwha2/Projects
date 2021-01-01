from typing import List
from sys import argv as argv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True

		def isMirror(p,q):
			if not p or not q:
				return not p and not q
			return p.val == q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left)
		return isMirror(root.left, root.right)


# argv[1]
# print(Solution())
