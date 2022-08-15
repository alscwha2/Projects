class Solution:
    def intToRoman(self, num: int) -> str:
        ones  = {0: "I", 1: "X", 2: "C", 3: "M"}
        fives = {0: "V", 1: "L", 2: "D"}

        result = ""
        for power in range(3, -1, -1):
            digit, num = divmod(num, 10 ** power)
            if digit == 4:
                result += ones[power] + fives[power]
            elif digit == 9:
                result += ones[power] + ones[power + 1]
            else:
                if digit >= 5:
                    result += fives[power]
                    digit -= 5
                for _ in range(digit):
                    result += ones[power]

        return result


print(Solution().intToRoman(58))