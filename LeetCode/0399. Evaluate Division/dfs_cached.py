from collections import defaultdict
from typing import List

'''
    The list of equations is a list of graph edges.
    We're looking for a path from Cj to Dj
    The weights of the edges are the values
    Multiply the weights of the edges as the final answer for each query
    
    The answer is dfs with caching
    
    The one part here that wasn't intuitive was that the reverse of the edge is
        1 / value
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
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

        def solve(equation):
            if equation in solved:
                return solved[equation]

            dividend, divisor = equation
            solved[equation] = -1.0
            for child in adjacency_lists[dividend]:
                if (value := solve((child, divisor))) != -1.0:
                    solved[equation] = solved[(dividend, child)] * value
                    break
            return solved[equation]

        return [solve(tuple(equation)) for equation in queries]