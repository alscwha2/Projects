# from typing import List
# from sys import List
from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
	Prettier version of previous solution
	If we define ListNode.__lt__ we don't have to use tuples

	Also realized that the heap is just a list so we could 
	 check that it is empty with heap == [] instead of try/catch

	Interestingly it ran about 10-15ms faster when using the tuple method.
	 I assume that that's because of the overhead of calling a function
	 as opposed to tuple creation/element access/integer comparison

'''

class Solution:
	# implement ListNode.__lt__ function so that ListNodes work in heap
	def lt(self: ListNode, other: ListNode):
		return self.val < other.val
	ListNode.__lt__ = lt

	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		# initialize heap
		heap = [node for node in lists if node is not None]
		heapify(heap)

		current = header = ListNode()
		# get next node, add to list, push its successor back on heap
		while heap != []:
			current.next = heappop(heap)
			current = current.next
			if current.next is not None: 
				heappush(heap, current.next)
		
		return header.next
		

# sys.argv[1]
# print(Solution())
