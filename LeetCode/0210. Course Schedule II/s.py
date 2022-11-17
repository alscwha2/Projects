from typing import List

"""
    Solution:
        Build directed graph of prereq -> course
        If has cycles:
            return []
        else:
            return topological_sort(graph)
        
        def topological sort:
            return postorder_dfs(transpose(graph))
        
        def transpose:
            for edge in graph:
                replace prereq -> couse with course -> prereq
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        transpose = [[] for _ in range(numCourses)]

        def populate_transpose():
            for course, prereq in prerequisites:
                transpose[course].append(prereq)

        populate_transpose()

        def postorder_dfs(graph: List[List[int]]) -> List[int]:
            """
            This function also check for cycles, and will return [] if cyclic
            :param graph:
            :return: postorder dfs traversal of graph, or [] if cyclic
            """
            has_cycle = False

            traversal = []
            seen = set()
            stack = []

            def traverse(node: int):
                nonlocal has_cycle
                seen.add(node)
                stack.append(node)
                for child in graph[node]:
                    if child in stack:
                        has_cycle = True
                        return
                    if child not in seen:
                        traverse(child)
                traversal.append(node)
                stack.pop()

            for node in range(numCourses):
                if node not in seen:
                    traverse(node)

            return [] if has_cycle else traversal

        def topological_sort() -> List[int]:
            return postorder_dfs(transpose)

        return topological_sort()
