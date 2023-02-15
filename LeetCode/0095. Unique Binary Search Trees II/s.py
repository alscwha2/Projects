from itertools import combinations
from functools import cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def add_number_to_tree(self, root, number, copy=None):
        if not root:
            return None
        if not copy:
            copy = TreeNode()
        copy.val = root.val + number
        copy.left = self.add_number_to_tree(root.left, number)
        copy.right = self.add_number_to_tree(root.right, number)
        return copy


    @cache
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]

        all_trees = []
        for left_children_number in range(n):
            root_val = left_children_number + 1
            right_children_number = n - root_val

            left_trees = self.generateTrees(left_children_number)
            right_trees = self.generateTrees(right_children_number)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    new_tree = TreeNode(root_val)
                    new_tree.left = left_tree
                    new_tree.right = self.add_number_to_tree(right_tree, root_val)
                    all_trees.append(new_tree)
        return all_trees

