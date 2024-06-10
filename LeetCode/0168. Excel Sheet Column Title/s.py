from math import log, floor


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        lookup = dict(zip(range(1, 27), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        lookup[0] = ''
        powers = floor(log(columnNumber, 26))
        power_amounts = []
        for i in range(powers, -1, -1):
            number, columnNumber = divmod(columnNumber, 26**i)
            power_amounts.append(number)
        power_amounts.reverse()
        for i in range(len(power_amounts)-1):
            amount = power_amounts[i]
            if amount < 1:
                power_amounts[i+1] -= 1
                power_amounts[i] += 26
        return ''.join(lookup[amount] for amount in power_amounts)[::-1]
