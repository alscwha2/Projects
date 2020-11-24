from typing import List
from sys import argv as argv
from collections import deque as deque
from collections import defaultdict as defaultdict
import heapq

'''
	Take the smallest lexical path
	Then expand all of the remaining loops and edpoint and insert
'''

class ListNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		nodes = dict()
		vertices = defaultdict(list)
		for ticket in tickets:
			vertices[ticket[0]].heappush(vertices[ticket[1]])

		# be greedy, will be left with cyles
		current = head = ListNode('JFK')
		while vertices[current]:
			children = vertices[current.val]
			current.next = ListNode(heappop(children))
			if not children:
				del vertices[current.val]
			current = current.next





# argv[1]
# print(Solution())