from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n-1:
            return False

        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        seen = [False for _ in range(n)]

        def dfs(node: int):
            seen[node] = True
            for neighbor in adjacency_list[node]:
                if not seen[neighbor]:
                    dfs(neighbor)

        dfs(0)
        return all(seen)