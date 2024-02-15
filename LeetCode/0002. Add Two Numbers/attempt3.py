'''
    This  is the fixed version of the iterable solution.
'''

from itertools import zip_longest

def __iter__(self):

    class ln_iter:
        def __init__(self, node):
            self.node = ListNode(val=None)
            self.node.next = node

        def _iter_(self):
            return self
            
        def __next__(self):
            next = self.node.next
            if self.node.next == None:
                raise StopIteration
            self.node = next
            return self.node.val

    return ln_iter(self)

ListNode.__iter__ = __iter__

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        sum_list = ListNode(val="sentinel")
        current = sum_list
        for pair in zip_longest(l1, l2, fillvalue=0):
        	tens, ones = divmod(sum(pair) + overflow, 10)
        	current.next = ListNode(ones)
        	current = current.next
        	overflow = tens
        if overflow:
            current.next = ListNode(overflow)
        return sum_list.next
