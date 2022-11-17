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

        ########################## FUNCTION DEFINITIONS ########################
        def edge_list_to_adjacency_list_transpose(edge_list: List[List[int]]):
            transpose = [[] for _ in range(numCourses)]
            for course, prereq in edge_list:
                transpose[course].append(prereq)

            return transpose

        def has_cycles(graph: List[List[int]], *, path=None, seen=None, next=None) -> bool:
            """
            :param graph:
            :param path: for internal use only.
            :param seen: for internal use only.
            :param next: for internal use only.
            :return: True if graph has cycle, else False
            """

            # For initial call to has_cycles, should have no keyword arguments
            if path is None:
                seen = set()
                return any(has_cycles(graph, path=[], seen=seen, next=node)
                           for node in range(numCourses))

            # if we have seen 'next' on this path then there is a cycle
            if next in path:
                return True

            # if we have seen 'next' and it is not on this path then
            #    it can't make a cycle, else we would have found the cycle when
            #    processing that node
            if next in seen:
                return False

            path.append(next)
            seen.add(next)
            answer = any(has_cycles(graph, path=path, seen=seen, next=child)
                         for child in graph[next])
            path.pop()  # clean-up data structure for the next call to use it
            return answer

        def postorder_dfs(graph: List[List[int]]) -> List[int]:
            """
            :param graph:
            :return: List[int] postorder dfs traversal of graph
            """
            traversal = []
            seen = set()

            def traverse(node: int):
                seen.add(node)
                for child in graph[node]:
                    if child not in seen:
                        traverse(child)
                traversal.append(node)

            for node in range(numCourses):
                if node not in seen:
                    traverse(node)

            return traversal

        def topological_sort(graph: List[List[int]]) -> List[int]:
            """
            :param graph:
            :return: [] if graph is empty or cyclic, else List[int] topological sort of grpah nodes
            """
            return [] if has_cycles(graph) else postorder_dfs(graph)

        ########################### APPLICATION LOGIC ##########################

        transpose = edge_list_to_adjacency_list_transpose(prerequisites)
        return topological_sort(transpose)


print(Solution().findOrder(2, [[1, 0], [0, 1]]))
