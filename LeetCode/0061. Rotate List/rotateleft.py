from typing import List
from sys import argv as argv

'''
	big fail, I implemented rotateLeft not rotateRight
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 0
        previous = None
        current = head
        while current:
        	length += 1
        	if k == 0:
        		newhead = current
        		if previous is not current:
        			previous.next = None
        		while current.next:
        			current = current.next
        		current.next = head
        		return newhead
        	k -= 1
        	previous = current
        	current = current.next
        
        if k:
        	k = k % length
        tail = previous
        current = head
        while k:
        	previous = current
        	current = current.next
        previous.next = None
        tail.next = head
        return current

# argv[1]
inputlist = [1,2,3,4,5]
inputhead = ListNode(-1)
current = inputhead
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

solutionlist = Solution().rotateRight(inputhead,2)
printstring = '['
while solutionlist:
	printstring += str(solutionlist.val) + ','
	solutionlist = solutionlist.next
print(printstring + ']')