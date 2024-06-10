from math import log, floor


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        lookup = dict(zip(range(1, 27), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        lookup[0] = '' # this is necessary


        powers = floor(log(columnNumber, 26))
        power_amounts = [(columnNumber // (26**i)) % 26 for i in range(powers+1)]

        for i in range(len(power_amounts)-1):
            amount = power_amounts[i]
            if amount < 1:
                power_amounts[i+1] -= 1
                power_amounts[i] += 26

        return ''.join(lookup[amount] for amount in power_amounts)[::-1]
