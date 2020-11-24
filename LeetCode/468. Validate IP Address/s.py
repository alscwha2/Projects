# from typing import List
# from sys import argv as argv
from string import hexdigits as hexdigits

class Solution:
	def validIPAddress(self, IP: str) -> str:
		# ---------------------- FUNCTIONS --------------------------
		def vf(IP: str) -> bool:
			tokens = IP.split('.')
			if len(tokens) != 4:
				return False

			for token in tokens:
				if not token.isnumeric():
					return False
				if token != '0' and token[0] == '0':
					return False
				if not 0 <= int(token) <= 255:
					return False
			return True

		def vs(IP: str) -> bool:
			tokens = IP.split(':')
			if len(tokens) != 8:
				return False

			for token in tokens:
				if not 1 <= len(token) <= 4:
					return False
				for c in token:
					if c not in hexdigits:
						return False
			return True

		# ---------------------- CODE STARTS HERE -------------------------------

		if '.' in IP[:4]:
			if vf(IP):
				return 'IPv4'
		else:
			if vs(IP):
				return 'IPv6'
		return 'Neither'

# argv[1]
# print(Solution().validIPAddress("01.01.01.01"))