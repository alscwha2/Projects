from itertools import pairwise
from typing import List

'''
failing conditions:
* if set(*chain(*sequences)) != set(nums)
* if there is more than one valid topological sort
* if there is no topological sort

Use Kahn's algorithm making sure that there is one and only one leaf every iteration
If there is more than one leaf then there will be multiple solutions
Through experimentation, it appears that the transpose of a graph with one and
    only one topological sort also has one and only one topological sort
'''


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        def nodes():
            return range(1, len(nums) + 1)

        adj_list = {node: set() for node in nodes()}
        transpose_adj_list = {node: set() for node in nodes()}

        def create_graph_and_transpose():
            for seq in sequences:
                for a, b in pairwise(seq):
                    adj_list[a].add(b)
                    transpose_adj_list[b].add(a)

        create_graph_and_transpose()

        topological_sort = []
        leaves = [node for node in nodes() if not transpose_adj_list[node]]

        def process(leaf):
            topological_sort.append(leaf)
            for parent in adj_list[leaf]:
                transpose_adj_list[parent].remove(leaf)
                if not transpose_adj_list[parent]:
                    leaves.append(parent)

        for _ in nodes():
            if len(leaves) != 1:
                return False
            process(leaves.pop())

        return topological_sort == nums



