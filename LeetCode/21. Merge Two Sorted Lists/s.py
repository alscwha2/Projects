from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toListNode(l: List[int]):
	head = ListNode(l.pop(0))
	current = head
	while l != []:
		current.next = ListNode(l.pop(0))
		current = current.next
	return head


class Solution:
	def lt(self, other: ListNode):
		return self.val < other.val
	ListNode.__lt__ = lt

	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		header = ListNode(-1)

		current = header
		while l1 is not None and l2 is not None:
			if l1 < l2:
				current.next = l1
				l1 = l1.next
			else:
				current.next = l2
				l2 = l2.next
			current = current.next
		current.next = l1 if l1 is not None else l2
		
		return header.next



head = Solution().mergeTwoLists(toListNode([1,2,4]),toListNode([1,3,4]))
while head is not None:
	print(head.val)
	head = head.next
