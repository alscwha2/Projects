"""
    Morris Traversal, O(n) time, O(1) space
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional [TreeNode]) -> int:
        total = 0
        current = root
        while current:
            if current.left:
                if not current.left.left and not current.left.right:
                    total += current.left.val
                    current = current.right
                else:
                    pred = current.left
                    while pred.right and pred.right != current:
                        pred = pred.right

                    if pred.right:
                        pred.right = None
                        current = current.right
                    else:
                        pred.right = current
                        current = current.left
            else:
                current = current.right
        return total
