from typing import List
from sys import argv as argv
from collections import defaultdict as defaultdict
from string import ascii_lowercase
'''
	TURNS OUT SOMEONE POSTED THIS SOLUTION ON THE SOLUTION PAGE 2 YEARS BEFORE ME! SO MUCH FOR BEING ORIGINAL...


	
	This solution is basically creating a Hashing function that only cares about the characters and doesn't care about their position in the string. 'abc', 'bca', 'cba' all hash to 30.

	- Multiplication is commutative, i.e. as long as we're multiplying the same numbers together the order doesn't matter. 2 * 3 * 5 == 2 * 5 * 3==3 * 5 * 2...
	- Assign each character a unique prime: a=2, b=3, c=5, d=7...
	- Calculate the product of each string, e.g. 'abc' = 2 * 3 * 5 == 30
	- Therefore: 'abc' == 2 * 3 * 5 == 3 * 5 * 2 == 'bca'
	- Any number can be expressed as a unique product of primes (google 'prime factorization' to learn more). E.g. The unique prime factorization of 30 is 2 * 3 * 5. So if I give you the number 30, you know that the characters used to make up that number must have been 2==a, 3==b, 5==c. In any order.
	- DUPLICATES: This also words for duplicates. 'aab' == 2 2 3 == 12. Only strings with 2 'a's and 1 'b' will produce 12.
	
	Iterate through the list of strings, calculate each product, save in a map mapping the calculated products with the strings that produced them.
'''

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		# assign each letter a unique prime
		primes = [2,3,5,7] + [n for n in range(11,121) if n%2 and n%3 and n%5 and n%7]
		letters = string.ascii_lowercase
		values = {letters[i] : primes[i] for i in range(len(letters))}

		groups = defaultdict(list)

		for str in strs:
			# find the product of all of the prime values
			product = 1
			for c in str:
				product *= values[c]

			# save it in the map
			groups[product].append(str)

		return [groups[p] for p in groups]



# argv[1]
# print(Solution()) 