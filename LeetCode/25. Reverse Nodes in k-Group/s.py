# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
	I think this is O(n/k) space because of all of the variables in the recursive calls
	You could do it in O(1) space by putting it into a while loop and just keeping track
		of the end of the previous segment in a variable
	But that would be less elegant
'''
class Solution:
	def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
		# check to make sure that there are enough free nodes to reverse:
		current = head
		for i in range(k):
			if current is None:
				return head
			current = current.next

		# actually go and do the reversing
		prev = head
		current = head.next
		for i in range(k-1):
			next = current.next
			current.next = prev

			prev = current
			current = next

		# at this point current fell off the edge
		# head is now the tail of the reversed segment
		head.next = self.reverseKGroup(current, k)
		# prev is now the head of the reversed segment
		return prev