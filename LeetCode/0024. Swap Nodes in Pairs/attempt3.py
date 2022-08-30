"""
    This code does away with the need to check that the head is not None
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        header = ListNode(-1, head)
        prev = None
        first = header
        second = head
        should_swap = False

        while second:
            if should_swap:
                prev.next = second
                first.next = second.next
                second.next = first

                second = first.next
                should_swap = False
            else:
                prev = first
                first = second
                second = second.next
                should_swap = True

        return header.next