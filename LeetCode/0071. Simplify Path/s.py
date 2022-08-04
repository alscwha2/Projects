from typing import List
from sys import argv as argv

class Solution:
	def simplifyPath(self, path: str) -> str:
		answer = ''
		to_go_back = 0
		path = path.split('/')
		for i in range(len(path)-1, -1, -1):
			dir = path[i]
			if dir == '' or dir == '.':
				continue
			elif dir == '..':
				to_go_back += 1
			elif to_go_back:
				to_go_back -= 1
			else:
				answer = '/' + dir + answer

		return answer if answer else '/'



# argv[1]
# print(Solution())
