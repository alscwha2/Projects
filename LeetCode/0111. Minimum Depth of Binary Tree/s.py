# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        secondary_queue = []
        height = 0
        while queue:
            height += 1
            while queue:
                node = queue.pop()
                if not node.left and not node.right:
                    return height
                if node.left:
                    secondary_queue.append(node.left)
                if node.right:
                    secondary_queue.append(node.right)
            queue = secondary_queue
            secondary_queue = []

