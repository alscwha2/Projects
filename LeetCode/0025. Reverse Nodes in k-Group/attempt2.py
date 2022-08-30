"""
    This is O(1) space.
    I see that for problems like these I am predisposed to doing them iteratively
        as opposed to recursively
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:  # code runs without this check, but it saves us work
            return head

        header = ListNode(-1, head)
        end_of_previous_segment = header
        beginning_of_current_segment = head

        current = head
        while True:
            # check that there are k nodes left to switch
            for _ in range(k):
                if not current:
                    return header.next
                current = current.next

            # reverse the nodes in the current segment
            prev = beginning_of_current_segment
            current = prev.next
            for _ in range(k - 1):
                next = current.next
                current.next = prev
                prev = current
                current = next

            # connect to previous and next segments
            end_of_previous_segment.next = prev
            beginning_of_current_segment.next = current

            # update segment variables for next iteration
            end_of_previous_segment = beginning_of_current_segment
            beginning_of_current_segment = current
