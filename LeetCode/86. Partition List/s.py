from typing import List
from sys import argv as argv

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def partition(self, head: ListNode, x: int) -> ListNode:
		smallhead = smalltail = ListNode(-1)
		bighead = bigtail = ListNode(-1)
		current = head
		while current:
			if current.val < x:
				smalltail.next = smalltail = current
			else:
				bigtail.next = bigtail = current
			current = current.next
		smalltail.next = bighead.next
		bigtail.next = None
		return smallhead.next

# argv[1]
# print(Solution())
