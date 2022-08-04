from typing import List

'''
	slight tweak to attempt2 (got from solution doc):
		just turn it into a ring and then break it in the right spot
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head or not k:
			return head

		length = 1
		current = head

		# iterate through to find the length and tail. first pass
		while current.next:
			length += 1
			current = current.next
		current.next = head
		previous = current
		current = head

		# calculate location of new head
		k %= length
		k = length-k

		# change head location. second pass
		for i in range(k):
			previous = current
			current = current.next
		previous.next = None
		return current



inputlist, amount = ([88,47,45,81,16,91,92,60],9)
current = inputhead = ListNode(-1)
for num in inputlist:
	current.next = ListNode(num)
	current = current.next
inputhead = inputhead.next

current = inputhead
printstring = '['
while current:
	printstring += str(current.val) + ','
	current = current.next
print(printstring + ']')

solutionlist = Solution().rotateRight(inputhead, amount)

printstring = '['
while solutionlist:
	printstring += str(solutionlist.val) + ','
	solutionlist = solutionlist.next
print(printstring + ']')