"""
    Redoing my original solution
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
        prev = header
        first = head
        second = head.next if head else None

        while first and second:
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            first = first.next
            second = first.next if first else second

        return header.next
