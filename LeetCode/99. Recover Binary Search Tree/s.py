from typing import List
from sys import argv as argv

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
        	return 
        # find the one that's out of place
        outofplace = []
        def test(parent, node):
        	if node.left:
        		if node.val < node.left.val:
        			outofplace.append((parent, node))
        		test(node, node.left)
        	if node.right:
        		if node.val > node.right.val:
        			outofplace.append((parent, node))
        		test(node, node.right)
        test(None, root)
        



# argv[1]
# print(Solution())
