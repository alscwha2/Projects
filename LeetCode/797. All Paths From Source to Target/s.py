from typing import List
from sys import argv as argv
from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        answer = []
        path = deque([0])

        def dfs():
            if path[-1] == n-1:
                answer.append(list(path))
            else:
                for neighbor in graph[path[-1]]:
                    path.append(neighbor)
                    dfs()
                    path.pop()
        dfs()
        return answer


# argv[1]
print(Solution())
