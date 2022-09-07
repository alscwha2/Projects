"""
    Have to convert everythign to negative in order to avoid overflow
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError("divisor may not be zero")

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_negative = divisor < 0 <= dividend or dividend < 0 <= divisor
        divisor = divisor if divisor < 0 else 0 - divisor
        dividend = dividend if dividend < 0 else 0 - dividend

        if dividend > divisor:
            return 0

        current_dividend = 0
        result = 0
        dividend = [int(digit) for digit in str(dividend)[:0:-1]]
        while dividend:
            if current_dividend > divisor:
                result = int(str(result) + "0")
                current_dividend = int(str(current_dividend) + "0")
                current_dividend -= dividend.pop()
            while current_dividend <= divisor:
                result -= 1
                current_dividend -= divisor

        if not is_negative:
            result = 0 - result

        return result

print(Solution().divide(-1, 1))