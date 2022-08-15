class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000, "": 2000}
        result = 0
        last_seen = ""
        for numeral in s:
            result += numerals[numeral]
            if numerals[last_seen] < numerals[numeral]:
                result -= 2 * numerals[last_seen]
            last_seen = numeral
        return result

print(Solution().romanToInt("XXI"))