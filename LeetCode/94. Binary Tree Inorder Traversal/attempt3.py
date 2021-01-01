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
		answer = []
		def inOrder(node):
			if node:
				inOrder(node.left)
				answer.append(node.val)
				inOrder(node.right)
		inOrder(root)
		return answer
		

# argv[1]
# print(Solution())
