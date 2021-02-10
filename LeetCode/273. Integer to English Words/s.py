from typing import List
from sys import argv as argv

class Solution:
	def numberToWords(self, num: int) -> str:
		if not num:
			return 'Zero'

		nums = {
			1 : 'One',
			2 : 'Two',
			3 : 'Three',
			4 : 'Four',
			5 : 'Five',
			6 : 'Six',
			7 : 'Seven',
			8 : 'Eight',
			9 : 'Nine',
			10 : 'Ten',
			11 : 'Eleven',
			12 : 'Twelve',
			13 : 'Thirteen',
			14 : 'Fourteen',
			15 : 'Fifteen',
			16 : 'Sixteen',
			17 : 'Seventeen',
			18 : 'Eighteen',
			19 : 'Nineteen'
		}

		ten = {
			2 : 'Twenty',
			3 : 'Thirty',
			4 : 'Forty',
			5 : 'Fifty',
			6 : 'Sixty',
			7 : 'Seventy',
			8 : 'Eighty',
			9 : 'Ninety'
		}
		def triple(num):
			answer = ''

			hundreds, num = divmod(num, 100)
			if hundreds: answer += nums[hundreds] + ' Hundred '

			tens, ones = divmod(num, 10)
			if tens > 1:
				answer += ten[tens] + ' '
				if ones: answer += nums[ones] + ' '
			else:
				if num: answer += nums[num] + ' '
				
			return answer

		magnitudes = {1000000000 : 'Billion ', 1000000 : 'Million ', 1000: 'Thousand ', 1 : ''}
		answer = ''
		for magnitude in magnitudes:
			amount, num = divmod(num, magnitude)
			if amount: answer += triple(amount) + magnitudes[magnitude]
		return answer[:len(answer)-1]

# argv[1]
print(Solution().numberToWords(123))