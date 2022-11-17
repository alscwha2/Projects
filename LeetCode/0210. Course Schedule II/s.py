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
                replace prereq -> course with course -> prereq
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def edge_list_to_adjacency_list_transpose(edge_list: List[List[int]]):
            transpose = [[] for _ in range(numCourses)]
            for course, prereq in edge_list:
                transpose[course].append(prereq)

            return transpose

        def postorder_dfs_without_cycles(graph: List[List[int]]) -> List[int]:
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

        def topological_sort(graph: List[List[int]]) -> List[int]:
            return postorder_dfs_without_cycles(graph)

        transpose = edge_list_to_adjacency_list_transpose(prerequisites)
        return topological_sort(transpose)
