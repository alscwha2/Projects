"""
Construct rooted tree.
DFS through the tree:
    passengers = 1 + number of children
    gallons = gallons_to_parent + sum(gallons spent by children)
    gallons_to_parent = math.ceil(passengers / seats)
    return passengers, gallons
"""
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List [List[int]], seats: int) -> int:
        def create_adjacency_list(edges: List[List[int]]):
            adjacency_list = [[] for _ in range(len(roads) + 1)]
            for a, b in edges:
                adjacency_list[a].append(b)
                adjacency_list[b].append(a)
            return adjacency_list

        roads = create_adjacency_list(roads)

        def root_tree(root):
            for child in roads[root]:
                roads[child].remove(root)
                root_tree(child)

        root_tree(0)
        
        def dfs(city):
            passengers = 1
            gallons = 0
            for child in roads[city]:
                child_passengers, child_gallons = dfs(child)
                passengers += child_passengers
                gallons += child_gallons
            gallons += math.ceil(passengers / seats)
            return passengers, gallons

        total = sum(dfs(city)[1] for city in roads[0])
        return total
