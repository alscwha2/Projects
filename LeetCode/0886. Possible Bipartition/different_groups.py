from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def create_adjacency_list(edges):
            adjacency_list = [[] for _ in range(n + 1)]
            for disliker, disliked in edges:
                adjacency_list[disliker].append(disliked)
                adjacency_list[disliked].append(disliker)
            return adjacency_list

        neighbors = create_adjacency_list(dislikes)

        groups = [-1 for _ in range(n+1)]
        other = {1: 2, 2: 1}

        def seen(node):
            return groups[node] != -1

        def possible(node, group=1):
            if seen(node):
                return groups[node] == group

            groups[node] = group
            return all(possible(neighbor, other[group]) for neighbor in neighbors[node])

        return all(possible(node) for node in range(1, n + 1) if not seen(node))
