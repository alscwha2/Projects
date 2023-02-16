# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        previous = None
        first_found = False
        second_found = False
        first = None
        second = None

        def traverse(root):
            nonlocal previous, first_found, first, second, second_found

            if root == None:
                return
            if first_found and second_found:
                return

            traverse(root.left)

            if not previous:
                previous = root

            if root.val < previous.val:
                if first_found:
                    second = root
                    second_found = True
                    return
                else:
                    first = previous
                    second = root
                    first_found = True
            previous = root
            
            traverse(root.right)

        traverse(root)
        first.val, second.val = second.val, first.val

