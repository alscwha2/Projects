class Solution:
	def isValid(self, s: str) -> bool:
		dic = {
			')' : '(',
			'}' : '{',
			']' : '['
		}

		stack = []
		for char in s:
			if char in dic.values(): stack.append(char)
			elif stack == [] or stack.pop() != dic[char]: return False

		return stack == [];