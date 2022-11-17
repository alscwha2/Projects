from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjacency_list = [set() for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].add(b)
            adjacency_list[b].add(a)

        leaves = [node for node in range(n) if len(adjacency_list[node]) == 1]

        while True:
            try:
                new_leaves = []
                for node in leaves:
                    neighbor = adjacency_list[node].pop()
                    adjacency_list[neighbor].remove(node)
                    if len(adjacency_list[neighbor]) == 1:
                        new_leaves.append(neighbor)
                if new_leaves:
                    leaves = new_leaves
                else:
                    break
            except KeyError:
                break

        return leaves


print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
