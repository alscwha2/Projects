'''
	ListNode should be iterable! That is the python way of doing it!
	Too bad, this isn't going to work on leetcode.
'''


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        sum_list = ListNode(val="sentinel")
        current = sum_list
        for pair in zip(l1, l2):
        	tens, ones = divmod(sum(pair) + overflow, 10)
        	current.next = ListNode(ones)
        	current = current.next
        	overflow = tens
        return sum_list.next

def construct_list(l):
	current = header = ListNode(-1)
	for elem in l:
		current.next = ListNode(elem)
		current = current.next
	return header.next

l1 = construct_list([2,4,3])
l2 = construct_list([5,6,4])

print(Solution.addTwoNumbers(None, l1, l2))
