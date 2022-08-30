"""
    Inspired by the Leetcode solution to cut out the second variable. Using :=
    This is probably as clear and concise as it could possibly get
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

        while first and (second := first.next):
            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            first = first.next

        return header.next

print(Solution().swapPairs(None))