from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def exec(l: List[int]):
	# print(l)
	if l is []: return None
	head = ListNode(l.pop(0))
	current = head
	for num in l:
		current.next = ListNode(num)
		current = current.next
	return head

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None: return l2
		if l2 is None: return l1
		if l1.val < l2.val:
			head = l1
			l1 = l1.next
		else:
			head = l2
			l2 = l2.next

		current = head
		# print(f'head: {head.val} curent: {current.val} l1: {l1.val} l2: {l2.val}')
		while l1 is not None and l2 is not None:
			if l1.val < l2.val:
				current.next = l1
				l1 = l1.next
			else:
				current.next = l2
				l2 = l2.next
			current = current.next
			l11 = l1.val if l1 is not None else None
			l22 = l2.val if l2 is not None else None
			# print(f'head: {head.val} curent: {current.val} l1: {l11} l2: {l22}')

		if l1 is None: current.next = l2
		else: current.next = l1

		return head

head = Solution().mergeTwoLists(exec([-9,3]), exec([5,7]))
while head is not None:
	# print(head.val)
	head = head.next


