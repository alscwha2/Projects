from functools import cache
from typing import List
from collections import defaultdict
"""
    This problem is reducible to whether or not there is a cycle in the 
        directed graph defined by the edges in the list.
    Note that direction of the edges doesn't matter, since the transpose of 
        a DAG is a DAG
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        children = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            children[prereq].append(course)

        seen = []

        @cache
        def has_cycles(node: int):
            seen.append(node)
            for child in children[node]:
                if child in seen or has_cycles(child):
                    return True
            seen.pop()
            return False

        return all(not has_cycles(course) for course in range(numCourses))