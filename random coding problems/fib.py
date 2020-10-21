from sys import argv
def fib(i: int):
	if i is 0 or i is 1: return i
	low = 0
	high = 1

	for i in range(i-1):
		new = low + high
		low = high
		high = new
	return high

for i in range(int(argv[1])):
	print(i, ": ", fib(i))