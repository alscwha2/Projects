from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        header = ListNode(-1, head)
        prev = header
        first = head
        second = head.next
        should_swap = True

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