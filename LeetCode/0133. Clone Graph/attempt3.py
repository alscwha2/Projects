"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        to_process = []
        old_to_new = {}

        def clone_node(node: 'Node') -> 'Node':
            new_node = Node(node.val)
            old_to_new[node] = new_node
            to_process.append((new_node, node.neighbors))
            return new_node

        new_root = clone_node(node)

        while to_process:
            current, neighbors = to_process.pop()
            for neighbor in neighbors:
                if neighbor not in old_to_new:
                    clone_node(neighbor)
                current.neighbors.append(old_to_new[neighbor])

        return new_root
