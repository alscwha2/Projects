from typing import List
"""
    The LeetCode people recommend this. This is very fast and uses no extra memory,
        but it also destroys the list...

    The next solution is a more elegant version of this one that I got off of someone one LC
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow = fast = head
        prev = None
        is_even = False
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                is_even = True
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        if not is_even:
            slow = slow.next

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
