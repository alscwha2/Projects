# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        total = 0
        def dfs(node):
            nonlocal total
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    return True
            if node.left and dfs(node.left):
                return True
            if node.right and dfs(node.right):
                return True
            total -= node.val
            return False
        return dfs(root)