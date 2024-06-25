from typing import List

"""
    Morris Traversal
    O(n) time (but does more work)
    O(1) space (since it's just using the space allocated to Null pointers)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        answer = []
        while current:
            if current.left:
                pred = current.left
                while pred.right and pred.right != current:
                    pred = pred.right
                if pred.right:
                    pred.right = None
                    answer.append(current.val)
                    current = current.right
                else:
                    pred.right = current
                    current = current.left
            else:
                answer.append(current.val)
                current = current.right
        return answer
