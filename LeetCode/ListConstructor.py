# Definition for singly-linked list.
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

def construct_list(l):
	current = header = ListNode(-1)
	for elem in l:
		current.next = ListNode(elem)
		current = current.next
	return header.next

def printList(l):
	print([elem for elem in l])