from typing import List
from collections import defaultdict


class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		"""
		dfs
		construct  adjacency list
		keep a stack of the edges that you used and remove then from the list
		when you move backwards add them back to the lisit and pop from stack
		if the stack reaches full then save that order
		compare all of the orders lexicographically

		Doing this the naive way is not feasable from a time standpoint
		There is a lot of repeated work being done, especially when there are
		multiple cycles over the same collection of nodes

		I think that we need to analyze the graph sort of as a kernel DAG. That
		when we encounter a cycle we log it and ignore it, leaving ourselves with
		a simple path through the itinerary with a bunch of cycles to figure out
		how to fit in.

		"""

		def edges_to_adjacency_list(edges):
			adj_list = defaultdict(list)
			for edge in edges:
				source, dest = edge
				adj_list[source].append(dest)
			return adj_list

		adjacency_list = edges_to_adjacency_list(tickets)
		available_tickets = edges_to_adjacency_list(tickets)

		valid_itineraries = []
		stack = ["JFK"]

		def dfs(airport):
			for dest in adjacency_list[airport]:
				if dest in available_tickets[airport]:
					available_tickets[airport].remove(dest)
					stack.append(dest)
					print(stack)
					if len(stack) == len(tickets)+1:
						valid_itineraries.append(stack.copy())
					else:
						dfs(dest)
					stack.pop()
					available_tickets[airport].append(dest)

		dfs("JFK")

		if len(valid_itineraries) >= 2:
			return min(valid_itineraries)
		return valid_itineraries[0]


tickets = [["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]
print(Solution().findItinerary(tickets))