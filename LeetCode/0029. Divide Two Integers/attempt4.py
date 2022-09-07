"""
    O(1) space using powers of 2 and bit manipulation.
    Note that right-shifting a negative numbers
        remains negative in python
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError("divisor may not be zero")

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_negative = divisor < 0 < dividend or dividend < 0 < divisor
        dividend = dividend if dividend < 0 else 0 - dividend
        divisor = divisor if divisor < 0 else 0 - divisor

        if dividend > divisor:
            return 0

        result = 0

        power = 0
        highest = divisor
        while highest >= -1073741824:
            next = highest << 1
            if next < dividend:
                break
            else:
                highest = next
                power += 1

        power_of_two = -1 << power

        for _ in range(power + 1):
            if highest >= dividend:
                dividend -= highest
                result += power_of_two
            power_of_two = power_of_two >> 1
            highest = highest >> 1

        if not is_negative:
            result = 0 - result

        return result




print(Solution().divide(10, 3))