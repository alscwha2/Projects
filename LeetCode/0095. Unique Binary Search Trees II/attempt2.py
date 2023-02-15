from itertools import product


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Using this optimization, we only call generateTrees with each number onnce
"""


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


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]

        all_trees = []
        for first_children_number in range(n // 2):
            second_children_number = n - first_children_number - 1

            first_trees = self.generateTrees(first_children_number)
            second_trees = self.generateTrees(second_children_number)
            for first_tree in first_trees:
                for second_tree in second_trees:
                    root_val = first_children_number + 1
                    new_tree = TreeNode(root_val)
                    new_tree.left = first_tree
                    new_tree.right = self.add_number_to_tree(second_tree, root_val)
                    all_trees.append(new_tree)

                    root_val = second_children_number + 1
                    new_tree = TreeNode(root_val)
                    new_tree.left = second_tree
                    new_tree.right = self.add_number_to_tree(first_tree, root_val)
                    all_trees.append(new_tree)
        if n % 2:
            num_children = n // 2
            root_val = num_children + 1
            child_trees = self.generateTrees(num_children)
            for right, left in product(child_trees, repeat=2):
                new_tree = TreeNode(root_val)
                new_tree.left = left
                new_tree.right = self.add_number_to_tree(right, root_val)
                all_trees.append(new_tree)
        return all_trees

