from typing import List

"""
Recursive dfs, failed for n == 200,000"""


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

        def dfs(node):
            if seen[node]:
                return False
            seen[node] = True
            if node == destination:
                return True
            return any(dfs(neighbor) for neighbor in adjacency_list[node])

        return dfs(source)






# print(Solution())
