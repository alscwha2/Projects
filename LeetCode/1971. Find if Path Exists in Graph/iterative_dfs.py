from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def construct_adjacency_list():
            adjacency_list = [[] for _ in range(n)]
            for a, b in edges:
                adjacency_list[a].append(b)
                adjacency_list[b].append(a)
            return adjacency_list

        adjacency_list = construct_adjacency_list()

        seen = [False] * n
        left_to_check = [source]
        while left_to_check:
            node = left_to_check.pop()
            seen[node] = True
            if node == destination:
                return True
            left_to_check.extend(neighbor for neighbor in adjacency_list[node] if not seen[neighbor])

        return False
