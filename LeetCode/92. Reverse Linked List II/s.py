from typing import List
from sys import argv as argv
from ListConstructor import ListNode, construct, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
		header = ListNode(-1, head)
		curr = header
		for i in range(m-2):
			curr = curr.next
		tail1 = curr
		head2 = tail2 = curr = curr.next
		next = curr.next
		for i in range(n-m):
			curr = next
			next = next.next
			curr.next = head2
			head2 = curr

		tail1.next = head2
		tail2.next = next
		return head


# argv[1]
printList(Solution().reverseBetween(construct([1,2,3,4,5]), 2, 4))