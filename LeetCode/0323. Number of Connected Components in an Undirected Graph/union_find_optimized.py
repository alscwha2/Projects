from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        membership = [node for node in range(n)]
        num_components = n

        def find(node: int) -> int:
            children = []
            while (parent := membership[node]) != node:
                children.append(node)
                node = parent
            for child in children:
                membership[child] = node
            return node

        def union(a: int, b: int) -> None:
            if find(a) != find(b):
                nonlocal num_components
                num_components -= 1
                membership[find(a)] = find(b)

        for edge in edges:
            union(*edge)

        return num_components

# print(Solution().countComponents(5,[[0,1],[1,2],[0,2],[3,4]]))