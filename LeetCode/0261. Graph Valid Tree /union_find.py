from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        is_tree = True

        components = [i for i in range(n)]

        def find(node):
            path = []
            while components[node] != node:
                path.append(node)
                node = components[node]
            for child in path:
                components[child] = node
            return node

        def union(a, b):
            nonlocal is_tree
            is_tree = is_tree and find(a) != find(b)
            components[find(a)] = find(b)

        for a, b in edges:
            union(a, b)

        return is_tree

print(Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]]))