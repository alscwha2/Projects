from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional [TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.right and not root.left:
            return [str(root.val)]
        return [f"{root.val}->" + path for path in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)]
