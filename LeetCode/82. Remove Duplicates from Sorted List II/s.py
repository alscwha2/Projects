from typing import List
from sys import argv as argv
from ListConstructor import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return head

		previous = header = ListNode(-1,head)
		current = head
		next = head.next

		while next:
			if next.val == current.val:
				while next and next.val == current.val:
					next = next.next
				previous.next = next
				if not next:
					break
			else:
				previous = current
			current = next
			next = next.next

		return header.next

# argv[1]
printList(Solution().deleteDuplicates(construct([1,2,3,3,4,4,5])))