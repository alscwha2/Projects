from typing import List

"""
    FIX THIS 
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
        while fast.next and fast.next.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            # slow, slow.next = slow.next, prev

        while prev and slow:
            print(prev, slow)
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        if prev or slow:
            return False
        return True

