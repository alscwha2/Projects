from typing import List
from sys import argv as argv

'''
	FAILED ATTEMPT AT MORRIS METHOD
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []

		def findPredecesor(node):
			node = node.left
			while node.right:
				node = node.right
			return node

		curr = root
		while curr:
			while curr.left:
				pred = findPredecesor(curr)
				pred.right = curr
				curr.left = None
				curr = root = pred
			curr = curr.right

		answer = []
		while root:
			answer.append(root.val)
			root = root.right

		return answer

		

# argv[1]
# print(Solution())
