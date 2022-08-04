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
		
		queue = deque([(root.left, root.right)])

		while queue:
			p,q = queue.pop()

			if not p or not q:
				if p or q:
					return False
				continue

			if p.val != q.val:
				return False

			queue.extendleft([(p.right,q.left), (p.left,q.right)])
		return True




# argv[1]
# print(Solution())
