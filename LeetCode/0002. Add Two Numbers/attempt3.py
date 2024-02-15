'''
    This  is the fixed version of the iterable solution.
'''

from itertools import zip_longest

def __iter__(self):

    class ln_iter:
        def __init__(self, node):
            self.node = node

        def _iter_(self):
            return self
            
        def __next__(self):
            if self.node == None:
                raise StopIteration
            value = self.node.val
            self.node = self.node.next
            return value

    return ln_iter(self)

ListNode.__iter__ = __iter__

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_list = ListNode(val="sentinel")

        current = sum_list
        overflow = 0
        for pair in zip_longest(l1, l2, fillvalue=0):
        	tens, ones = divmod(sum(pair) + overflow, 10)
        	current.next = ListNode(ones)
        	current = current.next
        	overflow = tens

        if overflow:
            current.next = ListNode(overflow)
        return sum_list.next
