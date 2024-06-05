from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional [TreeNode]) -> List[int]:
        if not root:
            return []
        answer  = self.postorderTraversal(root.left)
        answer += self.postorderTraversal(root.right)
        answer.append(root.val)
        return answer
