from typing import List
from sys import argv as argv
from collections import deque as deque
from collections import defaultdict as defaultdict
from heapq import heappush, heappop


class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		self.nodes = set([airport for flight in tickets for airport in flight])
		self.edges = defaultdict(list)
		for ticket in tickets:
			heappush(self.edges[ticket[0]], ticket[1])
		self.stack = deque()

		return self.dfs("JFK")


	def dfs(self, node: str) -> List[str]:
		self.stack.append(node)
		path = []
		cycles = []
		neighbors = self.edges[node]
		while neighbors != []:
			neighbor = heappop(neighbors)
			if neighbor in self.stack:
				path = [neighbor]
				continue
			next = self.dfs(neighbor)
			if next[-1] is node:
				cycles.append(next)
			else:
				path = next
		self.stack.pop()
		path = [node] + [n for cycle in cycles for n in cycle] + path
		return path






# argv[1]
Input= [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output= ["JFK","ATL","JFK","SFO","ATL","SFO"]
print(Solution().findItinerary(Input) == Output)
print("input:   ", Input)
print("output:  ", Solution().findItinerary(Input))
print("expected:", Output)
