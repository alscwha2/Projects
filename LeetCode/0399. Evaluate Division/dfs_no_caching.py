from collections import defaultdict
from itertools import chain
from typing import List

'''
    The list of equations is a list of graph edges.
    We're looking for a path from Cj to Dj
    The weights of the edges are the values
    Multiply the weights of the edges as the final answer for each query
    
    using caching:
        speed: O(M * N)
        space(O(N*2))
    caching increases speed for multiple queries at the cost of using a lot of space
    if you don't use caching, you'll do a lot of re-calculation of the same paths
        speed: O(M * N)
        space: O(N)
    
    The one part here that wasn't intuitive was that the reverse of the edge is
        1 / value
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set(chain(*equations))
        adjacency_lists = defaultdict(list)
        solved = {}

        def load_solved_equations_and_construct_adjacency_list():
            def load_solved_equation(equation):
                solved[tuple(equation)] = value
                solved[tuple(reversed(equation))] = 1 / value

            def add_to_adjacency_list(equation):
                dividend, divisor = equation
                adjacency_lists[dividend].append(divisor)
                adjacency_lists[divisor].append(dividend)

            for eq, value in zip(equations, values):
                load_solved_equation(eq)
                add_to_adjacency_list(eq)

        load_solved_equations_and_construct_adjacency_list()

        def if_not_seen(solve):
            seen = []

            def solve_if_not_seen(dividend, divisor):
                if dividend in seen:
                    return -1.0

                seen.append(dividend)
                answer = solve(dividend, divisor)
                seen.pop()
                return answer
            return solve_if_not_seen

        @if_not_seen
        def solve(dividend, divisor):
            if dividend == divisor:
                return 1.0

            for child in adjacency_lists[dividend]:
                if (value := solve(child, divisor)) != -1.0:
                    return solved[(dividend, child)] * value

            return -1.0

        return [solve(*equation) if all(node in nodes for node in equation) else -1.0 for equation in queries]


# print(Solution())
