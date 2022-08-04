# from typing import List
# from sys import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
	Simple recursive solution.
	Not the most efficient.
'''

class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		length = len(lists)
		if length is 0: return None
		if length is 1: return lists[0]
		if length is 2: return self.mergeTwoLists(lists[0], lists[1])
		return self.mergeTwoLists(self.mergeKLists(lists[:length//2]), self.mergeKLists(lists[length//2:]))

	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None: return l2
		if l2 is None: return l1
		current = l1 if l1.val < l2.val else l2
		if l1.val < l2.val: l1 = l1.next
		else: 				l2 = l2.next

		head = current

		while l1 is not None and l2 is not None:
			if l1.val < l2.val:
				current.next = l1
				current = current.next
				l1 = l1.next
			else:
				current.next = l2
				current = current.next
				l2 = l2.next

		if l1 is None: l1 = l2
		current.next = l1

		return head

# sys.argv[1]
# print(Solution())