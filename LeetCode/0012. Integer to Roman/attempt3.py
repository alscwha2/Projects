"""
With recursion
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        ones  = {0: "I", 1: "X", 2: "C", 3: "M"}
        fives = {0: "V", 1: "L", 2: "D", 3: ""}

        result = ""
        for power in range(3, -1, -1):
            digit, remainder = divmod(num, 10 ** power)
            has_five, num_ones = divmod(digit, 5)
            if num_ones == 4:
                return result + ones[power] + self.intToRoman(num + 10 ** power)
            result += fives[power] * has_five + ones[power] * num_ones
            num = remainder
        return result


print(Solution().intToRoman(58))