"""
    This problem is reducible to asking whether an odd numbered cycle exists.
    Algorithm:
        * Search for cycles
        * If odd:
            return false
        * else:
            continue
        * return True

    The solution on LeetCode points out that an easier way than testing for an
    odd cycle length is to just flip flop a boolean between even and odd until
    you get there
"""
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def create_adjacency_list(edges):
            adjacency_list = [[] for _ in range(n + 1)]
            for disliker, disliked in edges:
                adjacency_list[disliker].append(disliked)
                adjacency_list[disliked].append(disliker)
            return adjacency_list

        class Path:
            def __init__(self):
                self.count = 0
                self.map = [0 for _ in range(n+1)]

            def __len__(self):
                return self.count

            def __contains__(self, node):
                return self.map[node] != 0

            def add(self, node):
                self.count += 1
                self.map[node] = self.count

            def remove(self, node):
                self.count -= 1
                self.map[node] = 0

            def odd_cycle(self, node):
                cycle_length = self.count - self.map[node] + 1
                return cycle_length % 2 == 1

        neighbors = create_adjacency_list(dislikes)

        seen = [False] * (n+1)
        path = Path()

        def possible(node):
            if seen[node]:
                return not (node in path and path.odd_cycle(node))

            seen[node] = True
            path.add(node)
            if any(not possible(neighbor) for neighbor in neighbors[node]):
                return False
            path.remove(node)
            return True

        return all(possible(node) for node in range(1, n + 1) if not seen[node])
