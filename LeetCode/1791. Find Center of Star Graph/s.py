from typing import List


"""
The center will be in every edge, and only the center will be in more than one edge.
So just find the node that is in both of the first two edges"""


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        return a if a in edges[1] else b

# print(Solution())
