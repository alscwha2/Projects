from typing import List
from sys import argv as argv

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
        	next = current.next
        	current.next = prev
        	prev = current
        	current = next
        return prev


# argv[1]
# print(Solution())
