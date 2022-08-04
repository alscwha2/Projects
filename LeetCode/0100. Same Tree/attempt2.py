 from typing import List
from sys import argv as argv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		stack = deque([(p,q)])
		while stack:
			p,q = stack.pop()

			if not p or not q:
				if p or q:
					return False
				continue

			if p.val != q.val:
				return False

			stack.extend([(p.right,q.right), (p.left, q.left)])
		return True


# argv[1]
# print(Solution())
