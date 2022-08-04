from sys import argv
num = x = 625
for i in range(int(argv[1])):
	x = 0.5 * (x + num/x)
	print(x)