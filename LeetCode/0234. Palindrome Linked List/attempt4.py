from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        # Find the middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # At this point "slow" will either be pointing at the middle or at the beginning of the seond half.
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True

