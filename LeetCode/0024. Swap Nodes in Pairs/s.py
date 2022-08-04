# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def swapPairs(self, head: ListNode) -> ListNode:
		if head is None:
			return None

		prev = None
		first = head	
		second = head.next

		# need to update the head variable with the proper value because we're going to return it
		if second is not None:
			head = second

		
		while first is not None and second is not None:
			first.next = second.next
			second.next = first
			if prev is not None:
				prev.next = second

			# update variables for next iteration
			prev = first
			first = first.next
			if first is not None:
				second = first.next


		return head