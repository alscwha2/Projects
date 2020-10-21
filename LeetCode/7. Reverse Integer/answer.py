from sys import argv

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign

        newnum = 0
        while x is not 0:
        	newnum *= 10
        	newnum += x % 10
        	x //= 10

        newnum *= sign
        return newnum if -1 * 2 ** 31 <= newnum <= 2 ** 31 - 1 else 0

def rev(x: int) -> int:
	return Solution().reverse(x)

print(rev(eval(argv[1])))