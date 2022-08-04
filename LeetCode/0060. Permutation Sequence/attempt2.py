from typing import List
from sys import argv as argv
from ordered_set import OrderedSet

'''
	A problem with the first attempt is that since I was using a list I had to shift over all of the elements
	Let's change that with an ordered set
'''

class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		factorial = [1, 1] # list where each element is factorial of index

		# figure out what number factorial is just above OR EQUAL TO k
		b = 1
		while factorial[b] < k:
			b += 1
			factorial.append(factorial[b-1]*b)

		answer = ''.join([str(i) for i in range(1, n-b+1)])
		remaining = OrderedSet(i for i in range(n-b+1, n+1))

		while b > 0:
			# figure out which of the b digits to move here
			next_digit_indexindex = k // factorial[b-1]
			oneless = not k % factorial[b-1]
			if oneless:
				next_digit_indexindex -= 1

			# do the swap, keeping the tail in increasing order
			digit = remaining[next_digit_indexindex]
			remaining.remove(digit)
			answer += str(digit)

			# update k because we have already calculated part of the permutation
			k -= next_digit_indexindex * (factorial[b-1])
			# on to the next digit
			b -= 1
		return answer
'''
		# fac! is the smallest factorial <= k
		# therefore only the last FAC digits are going to be effected
		# let's go through it one digit at a time.
		# we do (TOT // (FAC-1)) + (TOT % (FAC-1)) <-- if the modula is >0 just add 1

		# once we reach FAC == 1 just return what you have
		# 

		1,2,3 - 1 0
		1,3,2 - 2 1
		2,1,3 - 3 2
		2,3,1 - 4 3
		3,1,2 - 5 4
		3,2,1 - 6 5

		1,2,3,4,5 - 1 0
		1,2,3,5,4 - 2 1
		1,2,4,3,5 - 3 2
		1,2,4,5,3 - 4 3 = 2 + 1
		1,2,5,3,4 - 5 4 = 2 + 2 = 4//2 4%2//1
		1,2,5,4,3 - 6 5 = 2 + 2 + 1
		1,3,2,4,5 - 7 6

		1,2,3,4 - 1
		1,2,4,3 - 2
		1,3,2,4 - 3
		1,3,4,2 - 4
		1,4,2,3 - 5
		1,4,3,2 - 6
		2,1,3,4 - 7
		2,1,4,3 - 8
		2,3,1,4 - 9
		2,3,4,1
		2,4,1,3
		2,4,3,1
		3,1,2,4

		# if it's equal to n!, then it's the reverse of the last n digits
		# if it's equal to n!+1, the it's n-1 and n swapped

		# find the factorial that is above or equal to k

'''
# argv[1]
print(Solution().getPermutation(9,3))
print(Solution().getPermutation(3,3))
print(Solution().getPermutation(4,9))	
print(Solution().getPermutation(3,5))	
print(Solution().getPermutation(4, 19))	