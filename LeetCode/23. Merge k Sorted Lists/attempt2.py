# from typing import List
# from sys import List
from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
	I think that the best solution would be to use a priority queue.

	
	add all nodes to pq
	head = pq.pop()
	if current.next is not None: pq.sink current.next

'''

class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		counter = 0
		if lists == []: return None
		heap = [(node.val, counter := counter + 1, node) for node in lists if node is not None]
		heapify(heap)

		if heap == []: return None

		head = heappop(heap)[2]
		current = head
		if current.next is not None: heappush(heap, (current.next.val, counter := counter + 1, current.next))

		while True:
			try:
				current.next = heappop(heap)[2]
				current = current.next
				if current.next is not None: heappush(heap, (current.next.val, counter := counter + 1, current.next))
			except IndexError:
				return head
		

# sys.argv[1]
# print(Solution())
