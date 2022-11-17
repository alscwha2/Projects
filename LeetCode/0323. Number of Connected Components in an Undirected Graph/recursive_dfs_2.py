from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def edges_to_adjacency(edges: List[List[int]]) -> List[List[int]]:
            adjacency_list = [[] for _ in range(n)]
            for a, b in edges:
                adjacency_list[a].append(b)
                adjacency_list[b].append(a)
            return adjacency_list

        neighbors = edges_to_adjacency(edges)
        seen = set()

        def dfs(node: int) -> None:
            seen.add(node)
            for neighbor in neighbors[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        num_components = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
            num_components += 1

        return num_components

