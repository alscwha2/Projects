# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# 
# Follow up: Could you do this in one pass?


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		head.previous = None
		previous = head
		current = head.next
		
		while current is not None:
			current.previous = previous
			previous = current
			current = current.next

		current = previous
		for i in range(n-1):
			current = current.previous
		if current is head: return current.next
		current.previous.next = current.next
		return head