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
        def is_leaf(node):
            return node and not node.left and not node.right

        def predecessor(node):
            pred = node.left
            while pred and pred.right and pred.right != node:
                pred = pred.right
            return pred

        total = 0
        current = root
        while current:
            if not current.left:
                current = current.right
            else:
                if is_leaf(current.left):
                    total += current.left.val
                    current = current.right
                else:
                    pred = predecessor(current)

                    if pred.right:
                        pred.right = None
                        current = current.right
                    else:
                        pred.right = current
                        current = current.left
        return total
